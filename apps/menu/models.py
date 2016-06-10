import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.dispatch import receiver

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

def upload_location(instance, filename):
    filename = str(uuid.uuid4())[:13] + '_' + filename
    return "menu/{0}".format(filename)


class Menu(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    description = models.TextField(null=False, blank=False, verbose_name='Описание')
    detail = JSONField(null=False, blank=False, verbose_name='Детально')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    photo = VersatileImageField(upload_to=upload_location, null=True, blank=True, verbose_name='Фото')
    is_lunch = models.BooleanField(default=False, null=False, blank=True, verbose_name='Бизнесс ланч')
    is_active = models.BooleanField(default=True, null=False, blank=True, verbose_name='Активированно')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Price(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='prices', verbose_name='Меню')
    count = models.FloatField(null=False, blank=False, verbose_name='Количество')
    measure = models.CharField(max_length=64, null=False, blank=False, verbose_name='Ед. измерения')
    value = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name='Значение')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимость'


@receiver(models.signals.post_save, sender=Menu)
def warm_Menu_photo_images(sender, instance, **kwargs):
    menu_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='menu_photo',
        image_attr='photo'
    )
    num_created, failed_to_create = menu_img_warmer.warm()
