import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone


def validate_not_past(value):
    if value < timezone.now():
        raise ValidationError('Дата не может быть меньше текущей')


def validate_datetime(value):
    datetime_regex = re.compile(
        r'^\d{4}-\d{2}-\d{2} [0-1][0-9]|[2][0-3]:[0-5][0-9]:[0-5][0-9]$'
    )
    if not datetime_regex.match(value):
        raise ValidationError('Неверный формат даты и времени')


phone_number_regex = RegexValidator(
    regex=r"^\+?1?\d{8,15}$",
    message=(
        "Номер телефона должен быть в формате: '+999999999'."
        "Допустимо от 9 до 15 цифр.")
)
