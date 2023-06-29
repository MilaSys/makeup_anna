from django.db import models


class Feedback(models.Model):
    """
    Модель таблицы тэга.
    Attributes:
        name: CharField - имя
        phone: CharField - номер телефона для связи
        created_at: DateTimeField - дата создания
    """

    name = models.CharField(
        verbose_name='Имя',
        max_length=16,
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=20,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата загрузки изображения',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-created_at']
