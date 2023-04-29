import phonenumbers
from django.db import models
from django.core.validators import validate_datetime

from feedback.strings import ERR_PHONENUMBER
from feedback.validators import validate_not_past


class Feedback(models.Model):
    """
    Модель таблицы тэга.
    Attributes:
        name: CharField - имя
        phone: CharField - номер телефона для связи
        message: TextField - пожелания/краткая информация
        created_at: DateTimeField - дата создания
    """

    name = models.CharField(
        verbose_name='Имя',
        max_length=100,
        help_text='Введите ваше имя.',
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=20,
        help_text='Введите номер телефона для связи.'
    )
    message = models.TextField(
        verbose_name='Информация',
        max_length=200,
        help_text='''Напишите здесь информацию
         о которой необходимо знать мастеру.''',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата загрузки изображения',
        auto_now_add=True,
    )

    def clean(self):
        try:
            parsed_number = phonenumbers.parse(self.phone, 'RU')
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValueError(ERR_PHONENUMBER)
            self.phone = phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            raise ValueError(ERR_PHONENUMBER)


class Сountdown(models.Model):
    """
    Модель таблицы тэга.
    Attributes:
        date: DateTimeField - Дата и время окончания акции
    """

    date = models.DateTimeField(
        verbose_name='Дата и время окончания акции',
        auto_now_add=False,
        blank=True,
        null=True,
        validators=[validate_datetime, validate_not_past],
        help_text='''Введите дату и время окончания акции
        в формате 2022-02-22 22:22:22.''',
    )
