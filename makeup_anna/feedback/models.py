import phonenumbers
from django.db import models

from feedback.strings import ERR_PHONENUMBER


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
        verbose_name="Имя",
        max_length=100,
        help_text="Введите ваше имя."
    )
    phone = models.CharField(
        verbose_name="Номер телефона",
        max_length=20,
        help_text="Введите номер телефона для связи."
    )
    message = models.TextField(
        verbose_name="Информация",
        max_length=200,
        help_text="""Напишите здесь информацию
         о которой необходимо знать мастеру."""
    )
    created_at = models.DateTimeField(
        verbose_name="Дата загрузки изображения",
        auto_now_add=True,
    )

    def clean(self):
        try:
            parsed_number = phonenumbers.parse(self.phone, "RU")
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValueError(ERR_PHONENUMBER)
            self.phone = phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            raise ValueError(ERR_PHONENUMBER)
