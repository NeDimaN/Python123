from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError("Длина превыщает 200 символов")

        return title

    class Meta:
        model = Active
        fields = ['title', 'slug', 'content', 'km', 'time', 'min_pulse', 'av_pulse', 'max_pulse', 'photo',
                  'is_published', 'cat']

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-input"}),
            'slug': forms.TextInput(attrs={"class": "form-input"}),
            'content': forms.Textarea(attrs={"cols": 60, "rows": 20, "class": "form-input"}),
            'km': forms.TextInput(attrs={"class": "form-input"}),
            'time': forms.TextInput(attrs={"class": "form-input"}),
            'min_pulse': forms.TextInput(attrs={"class": "form-input"}),
            'av_pulse': forms.TextInput(attrs={"class": "form-input"}),
            'max_pulse': forms.TextInput(attrs={"class": "form-input"}),

        }
