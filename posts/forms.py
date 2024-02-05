from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    content = forms.CharField(widget=forms.Textarea,required=True)
    thumbnail = forms.ImageField(required=True)
    class Meta:
        model = Post
        fields = ['title', 'content','thumbnail']
