import uuid

from django.db import models
from django.dispatch import receiver

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

from apps.events.models import Event
from .managers import GalleryManager


def upload_location(instance, filename):
    year, month = instance.created_at.year, instance.created_at.month
    filename = str(uuid.uuid4())[:13] + '_' + filename
    return "gallery/{0}/{1}/{2}".format(year, month, filename)


def album_upload_location(instance, filename):
    year, month = instance.created_at.year, instance.created_at.month
    filename = str(uuid.uuid4())[:13] + '_' + filename
    return "album/{0}/{1}/{2}".format(year, month, filename)


class Album(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    main_image = VersatileImageField(upload_to=album_upload_location, null=False, blank=False, verbose_name='Фото')
    event = models.ForeignKey(Event, related_name='album', null=False, blank=False, verbose_name='Мероприятие')

    objects = models.Manager()
    related_objects = GalleryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['-created_at']


class Image(models.Model):
    info = models.CharField(max_length=255, null=True, blank=True, verbose_name='Информация')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='images', null=False, blank=False, verbose_name='Альбом')
    image = VersatileImageField(upload_to=upload_location, null=False, blank=False, verbose_name='Фото')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


@receiver(models.signals.post_save, sender=Image)
def warm_gallery_image_images(sender, instance, **kwargs):
    gallery_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='gallery_image',
        image_attr='image'
    )
    num_created, failed_to_create = gallery_img_warmer.warm()


@receiver(models.signals.post_save, sender=Album)
def warm_album_image_images(sender, instance, **kwargs):
    album_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='album_image',
        image_attr='main_image'
    )
    num_created, failed_to_create = album_img_warmer.warm()
