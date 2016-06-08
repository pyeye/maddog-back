import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.dispatch import receiver

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


def upload_location(instance, filename):
    year, month = instance.date.year, instance.date.month
    filename = str(uuid.uuid4())[:13] + '_' + filename
    return "events/{0}/{1}/{2}".format(year, month, filename)


class Event(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название')
    artists = models.CharField(max_length=255, null=False, blank=False, verbose_name='Артисты')
    style = models.CharField(max_length=255, null=False, blank=False, verbose_name='Стиль')
    info = models.TextField(null=True, blank=True, verbose_name='Дополнительная информация')
    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    start = models.TimeField(null=False, blank=False, verbose_name='Начало')
    discounts = models.CharField(max_length=255, null=True, blank=True, verbose_name='Акции')
    price = models.IntegerField(default=0, null=False, blank=True, verbose_name='Вход')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    is_special = models.BooleanField(default=False, null=False, blank=True, verbose_name='Особенное мероприятие')
    is_active = models.BooleanField(default=True, null=False, blank=True, verbose_name='Активировано')
    poster = VersatileImageField(upload_to=upload_location, null=True, blank=True, verbose_name='Афиша')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


@receiver(models.signals.post_save, sender=Event)
def warm_Event_poster_images(sender, instance, **kwargs):
    event_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='event_poster',
        image_attr='poster'
    )
    num_created, failed_to_create = event_img_warmer.warm()
