from django import forms

from gallery.models import Gallery, Tag


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image', 'tags']

    image = forms.ImageField()
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all()
    )

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.content_type.startswith('image/'):
                raise forms.ValidationError(
                    'Загрузите изображение, пожалуйста.'
                )
        return image
