import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.dispatch import receiver

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

from .managers import NewsManager


def upload_location(instance, filename):
    year, month = instance.created_at.year, instance.created_at.month
    filename = uuid.uuid4().hex + '.jpg'
    return "news/{0}/{1}/{2}".format(year, month, filename)


class News(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(null=False, blank=False, verbose_name='Описание')
    category = models.ForeignKey('Category', related_name='news', verbose_name='Категория')
    created_at = models.DateField(auto_now_add=True, null=False, blank=True, verbose_name='Созданно')
    updated_at = models.DateField(auto_now=True, null=False, blank=True, verbose_name='Обновленно')
    is_active = models.BooleanField(default=True, null=False, blank=True, verbose_name='Активировано')
    image = VersatileImageField(upload_to=upload_location, null=True, blank=True, verbose_name='Изображение')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    objects = models.Manager()
    related_objects = NewsManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-updated_at']


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



@receiver(models.signals.post_save, sender=News)
def warm_event_poster_images(sender, instance, **kwargs):
    news_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='news_image',
        image_attr='image'
    )
    num_created, failed_to_create = news_img_warmer.warm()
