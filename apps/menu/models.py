import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

from .managers import MenuManager


def menu_upload_location(instance, filename):
    filename = str(uuid.uuid4())[:13] + '_' + filename
    return "menu/main/{0}".format(filename)


def set_upload_location(instance, filename):
    filename = str(uuid.uuid4())[:13] + '_' + filename
    return "menu/set/{0}".format(filename)


class Menu(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    description = models.TextField(null=False, blank=False, verbose_name='Описание')
    category = models.ForeignKey('Category', related_name='menu', verbose_name='Категория')
    detail = JSONField(null=True, blank=True, verbose_name='Детально')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    photo = VersatileImageField(upload_to=menu_upload_location, null=True, blank=True, verbose_name='Фото')
    photo_base64 = models.CharField(max_length=255, null=False, blank=True, default='base', verbose_name='Фото Base64')
    is_active = models.BooleanField(default=True, null=False, blank=True, verbose_name='Активированно')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    objects = models.Manager()
    related_objects = MenuManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Set(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    description = models.TextField(null=False, blank=False, verbose_name='Описание')
    menu = models.ManyToManyField('Menu', through='MenuSet', related_name='menus', verbose_name='Позиции меню')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    photo = VersatileImageField(upload_to=set_upload_location, null=True, blank=True, verbose_name='Фото')
    photo_base64 = models.CharField(max_length=255, null=False, blank=True, default='base', verbose_name='Фото Base64')
    is_active = models.BooleanField(default=True, null=False, blank=True, verbose_name='Активированно')
    additional = ArrayField(base_field=models.CharField(max_length=128), null=True, blank=True, verbose_name='Дополнительные блюда')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Набор'
        verbose_name_plural = 'Наборы'


class MenuSet(models.Model):
    set = models.ForeignKey('Set', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    menu_count = models.IntegerField(default=1, null=False, blank=True,)


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    group = models.ForeignKey('Group', related_name='category', verbose_name='Группа')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Group(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    code = models.CharField(max_length=128, null=False, unique=True, blank=False, verbose_name='Код')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Price(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True, related_name='prices', verbose_name='Меню')
    set = models.ForeignKey(Set, on_delete=models.CASCADE, blank=True, null=True, related_name='prices', verbose_name='Набор')
    count = models.FloatField(null=False, blank=False, verbose_name='Количество')
    measure = models.CharField(max_length=64, null=False, blank=False, verbose_name='Ед. измерения')
    value = models.IntegerField(null=False, blank=False, verbose_name='Значение')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return str(self.value)

    def clean(self):
        if sum(map(bool, [self.menu, self.set])) != 1:
            raise ValidationError('Необходимо ввести одну связанную таблицу')

    class Meta:
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимость'


@receiver(models.signals.post_save, sender=Menu)
def warm_menu_photo_images(sender, instance, **kwargs):
    menu_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='menu_photo',
        image_attr='photo'
    )
    num_created, failed_to_create = menu_img_warmer.warm()


@receiver(models.signals.post_save, sender=Set)
def warm_set_photo_images(sender, instance, **kwargs):
    set_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='set_photo',
        image_attr='photo'
    )
    num_created, failed_to_create = set_img_warmer.warm()
