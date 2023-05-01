import re
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_not_past(value):
    if value < timezone.now():
        raise ValidationError('Дата не может быть меньше текущей')


def validate_datetime(value):
    datetime_regex = re.compile(
        r'^\d{4}-\d{2}-\d{2} [0-1][0-9]|[2][0-3]:[0-5][0-9]:[0-5][0-9]$'
    )
    if not datetime_regex.match(value):
        raise ValidationError('Неверный формат даты и времени')
