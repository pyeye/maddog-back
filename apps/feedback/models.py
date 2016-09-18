from django.db import models
from django.contrib.postgres.fields import JSONField


class Feedback(models.Model):

    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    contact = models.CharField(max_length=255, null=True, blank=True, verbose_name='Контакт')
    message = models.TextField(null=False, blank=False, verbose_name='Сообщение')
    extra = JSONField(default={}, null=False, blank=True, verbose_name='Экстра')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
