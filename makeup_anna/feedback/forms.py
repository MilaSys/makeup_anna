import phonenumbers
import re
from django import forms

from feedback.models import Feedback
from feedback.strings import ERR_PHONENUMBER


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'message']

    def clean_name(self):
        value = self.cleaned_data['name']

        if not re.match(r'^[a-zA-Z]{2,}$', value):
            raise forms.ValidationError(
                'Введите имя!'
            )

        return value

    def clean_phone(self):
        phone_number = self.cleaned_data['phone']

        try:
            parsed_number = phonenumbers.parse(phone_number, 'RU')
            if not phonenumbers.is_valid_number(parsed_number):
                raise forms.ValidationError(ERR_PHONENUMBER)
            return phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164
            )
        except phonenumbers.NumberParseException:
            raise forms.ValidationError(ERR_PHONENUMBER)

    def clean_message(self):
        message = self.cleaned_data['message']

        if len(message.split()) < 2:
            raise forms.ValidationError(
                'Сообщение должно содержать не меньше 2х слов.'
            )

        return message
