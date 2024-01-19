from django import forms
from .models import Image


class GalleryItemForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'image']
