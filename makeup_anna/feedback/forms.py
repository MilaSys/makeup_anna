from django import forms
from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'type': 'text',
                    'name': 'name',
                    'placeholder': 'Введите имя',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'type': 'text',
                    'name': 'phone',
                    'placeholder': 'Введите телефон',
                }
            )
        }
