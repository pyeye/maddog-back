from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import JSONField


class Reservation(models.Model):

    STATUS_WAITING = 'w'
    STATUS_CONFIRMED = 'c'
    STATUS_DENIED = 'd'
    STATUS_CHOICES = (
        (STATUS_WAITING, 'Ожидает'),
        (STATUS_CONFIRMED, 'Подтверждено'),
        (STATUS_DENIED, 'Отменено'),
    )

    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    time = models.TimeField(null=False, blank=False, verbose_name='Время')
    is_vip = models.BooleanField(default=False, null=False, blank=True, verbose_name='VIP')
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{4,17}$', message="Номер телефона должен иметь следующий фомат: '+999999999'. до 15 цифр.")
    phone_number = models.CharField(max_length=17, null=True, blank=False, verbose_name='Телефон')
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Имя')
    deposite = models.PositiveIntegerField(null=True, blank=True, verbose_name='Депозит')
    count_people = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Количество человек')
    status = models.CharField(max_length=2, default=STATUS_WAITING, choices=STATUS_CHOICES, null=False, blank=True, verbose_name='Статус')
    comment = models.TextField(null=True, blank=True, verbose_name='Коментарий')
    extra = JSONField(default={}, null=False, blank=True, verbose_name='Экстра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
