from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name','last_name','phone_number','national_code')






