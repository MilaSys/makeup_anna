from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_not_past(value):
    if value < timezone.now():
        raise ValidationError('Дата не может быть меньше текущей')
