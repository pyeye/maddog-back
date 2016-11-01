import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

from .managers import EventsManager


def upload_location(instance, filename):
    year, month = instance.date.year, instance.date.month
    filename = str(uuid.uuid4())[:13] + '_' + filename
    return "events/{0}/{1}/{2}".format(year, month, filename)


def artists_upload_location(instance, filename):
    name = slugify(instance.name, allow_unicode=True)
    return "artists/{0}/{1}".format(name, filename)


class Event(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название')
    artists = models.ManyToManyField('Artist', related_name='artists', verbose_name='Артисты')
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

    objects = models.Manager()
    related_objects = EventsManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Artist(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name='Название')
    style = models.CharField(max_length=255, null=False, blank=False, verbose_name='Стиль')
    bio = models.TextField(null=True, blank=True, verbose_name='Биография')
    img = VersatileImageField(upload_to=artists_upload_location, null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'



@receiver(models.signals.post_save, sender=Event)
def warm_event_poster_images(sender, instance, **kwargs):
    event_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='event_poster',
        image_attr='poster'
    )
    num_created, failed_to_create = event_img_warmer.warm()

@receiver(models.signals.post_save, sender=Artist)
def warm_artist_images(sender, instance, **kwargs):
    artist_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='artist_img',
        image_attr='img'
    )
    num_created, failed_to_create = artist_img_warmer.warm()
