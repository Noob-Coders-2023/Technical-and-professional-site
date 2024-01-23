from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator
messages = {
    "required": 'لطفا این فیلد را پر کنید',
    'invalid': 'لطفا کارکتر معتبر وارد کنید',
    'max_length': "تعداد کارکتر های ورودی بیشتر از حد مجاز است",
    'min_length': 'تعداد کاراکترهای ورودی کمتر از حد مجاز است',

}


class SignupForm(UserCreationForm):
    messages = {
        "required": _('لطفاً این فیلد را پر کنید'),
        'invalid': _('لطفاً یک مقدار معتبر وارد کنید'),
        'max_length': _('تعداد کاراکترها بیشتر از حد مجاز است'),
        'min_length': _('تعداد کاراکترها کمتر از حد مجاز است'),
    }
    email = forms.EmailField(max_length=200, error_messages=messages)
    username = forms.CharField(error_messages=messages)
    first_name = forms.CharField(error_messages=messages)
    last_name = forms.CharField(error_messages=messages)
    phone_number = forms.CharField(error_messages=messages,validators=[RegexValidator(regex=r'09\d{9}', message='شماره موبایل معتبر نیست')])
    national_code = forms.CharField(error_messages=messages)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name','last_name','phone_number','national_code')







class CustomUserChangeForm(UserChangeForm):
    messages = {
        "required": _('لطفاً این فیلد را پر کنید'),
        'invalid': _('لطفاً یک مقدار معتبر وارد کنید'),
        'max_length': _('تعداد کاراکترها بیشتر از حد مجاز است'),
        'min_length': _('تعداد کاراکترها کمتر از حد مجاز است'),
    }
    email = forms.EmailField(max_length=200, error_messages=messages)
    username = forms.CharField(error_messages=messages)
    first_name = forms.CharField(error_messages=messages)
    last_name = forms.CharField(error_messages=messages)
    phone_number = forms.CharField(error_messages=messages)
    national_code = forms.CharField(error_messages=messages)
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'national_code')

