from django.db import models
from django.utils import timezone


class Action(models.Model):
    """
    Модель таблицы тэга.
    Attributes:
        date: DateTimeField - Дата и время окончания акции
        discount: IntegerField - Размер скидки
    """

    date = models.DateTimeField(
        verbose_name='Дата и время окончания акции',
        auto_now_add=False,
        default=timezone.now,
        help_text='''Введите дату и время окончания акции
        в формате 2022-02-22 22:22:22.''',
    )
    discount = models.IntegerField(
        verbose_name='Скидка',
        default='10',
    )

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        ordering = ['-date']
