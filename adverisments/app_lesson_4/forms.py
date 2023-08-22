from django import forms
from .models import Adverisments
from django.core.exceptions import ValidationError


# class AdvertismentForm (forms.Form):
#     title = forms.CharField(max_length=64)
#     description = forms.CharField(widget=forms.Textarea)
#     price = forms.DecimalField()
#     auction = forms.BooleanField(required=False)
#     image = forms.ImageField()


class AdvertismentForm(forms.ModelForm):
    class Meta:
        model = Adverisments
        fields = ['title', 'description', 'price', 'auction', 'image']

    def clean_title(self):
        data = self.cleaned_data['title']
        if data.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с вопросительного знака')
        return data
