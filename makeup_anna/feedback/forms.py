import phonenumbers
from django import forms

from feedback.models import Feedback
from feedback.strings import ERR_PHONENUMBER


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'message']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Имя обязательно")
        return name

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
