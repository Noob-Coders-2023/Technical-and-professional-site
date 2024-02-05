from django import forms
from .models import Image


class GalleryItemForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea,required=True)
    image = forms.ImageField(required=True)
    class Meta:
        model = Image
        fields = ['title', 'description', 'image']
