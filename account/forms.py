from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm
messages = {
    "required": 'لطفا این فیلد را پر کنید',
    'invalid': 'لطفا کارکتر معتبر وارد کنید',
    'max_length': "تعداد کارکتر های ورودی بیشتر از حد مجاز است",
    'min_length': 'تعداد کاراکترهای ورودی کمتر از حد مجاز است',

}



class SignupForm(UserCreationForm):
    GENDER_CHOICES = (
        ('w', 'مونث'),
        ('m', 'مذکر'),

    )
    captcha = CaptchaField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput,required=True)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)
    email = forms.EmailField(label='ایمیل', required=True)
    phone_number = forms.CharField(label='شماره تلفن', required=True)
    username=forms.CharField(label='نام کاربری',required=True)
    first_name=forms.CharField(label='نام ',required=True)
    last_name=forms.CharField(label='نام خانوادگی ',required=True)
    national_code=forms.CharField(label='شماره کارت ملی',required=True)
    gender = forms.ChoiceField(label='جنسیت', choices=GENDER_CHOICES, required=True)
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', "last_name", 'phone_number', 'national_code', 'gender','captcha')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('رمز عبور یکسان نیست')

        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(help_text='شما نمی توانید رمز عبور خود را در اینجا تغییر دهید')
    messages = {
        "required": _('لطفاً این فیلد را پر کنید'),
        'invalid': _('لطفاً یک مقدار معتبر وارد کنید'),
        'max_length': _('تعداد کاراکترها بیشتر از حد مجاز است'),
        'min_length': _('تعداد کاراکترها کمتر از حد مجاز است'),
    }
    captcha = CaptchaField()
    username = forms.CharField(error_messages=messages)
    first_name = forms.CharField(error_messages=messages)
    last_name = forms.CharField(error_messages=messages)
    phone_number = forms.CharField(error_messages=messages)
    national_code = forms.CharField(error_messages=messages)
    email = forms.EmailField(max_length=200, error_messages=messages)
    def clean_email(self):
        user=User.objects.get(phone_number=self.initial["phone_number"])
        email=self.cleaned_data['email']
        if user.email ==email:
            return email


        user=User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('این ایمیل قبلا استفاده شده است')
        return email



    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'national_code', "password")


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 1000, 'max': 9999, 'step': 1, 'type': 'number'}),
        min_value=1000,
        max_value=9999,
        localize=True,
    )
class CaptchaAuthenticationForm(AuthenticationForm):
    captcha = CaptchaField()

