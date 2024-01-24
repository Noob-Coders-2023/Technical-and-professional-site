from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
messages = {
    "required": 'لطفا این فیلد را پر کنید',
    'invalid': 'لطفا کارکتر معتبر وارد کنید',
    'max_length': "تعداد کارکتر های ورودی بیشتر از حد مجاز است",
    'min_length': 'تعداد کاراکترهای ورودی کمتر از حد مجاز است',

}


#
# class SignupForm(UserCreationForm):
#     messages = {
#         "required": _('لطفاً این فیلد را پر کنید'),
#         'invalid': _('لطفاً یک مقدار معتبر وارد کنید'),
#         'max_length': _('تعداد کاراکترها بیشتر از حد مجاز است'),
#         'min_length': _('تعداد کاراکترها کمتر از حد مجاز است'),
#     }
#     email = forms.EmailField(max_length=200, error_messages=messages)
#     username = forms.CharField(error_messages=messages)
#     first_name = forms.CharField(error_messages=messages)
#     last_name = forms.CharField(error_messages=messages)
#     phone_number = forms.CharField(error_messages=messages,validators=[RegexValidator(regex=r'09\d{9}', message='شماره موبایل معتبر نیست')])
#     national_code = forms.CharField(error_messages=messages)
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2','first_name','last_name','phone_number','national_code')
#

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confrim password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', "last_name", 'phone_number', 'national_code',)

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
    email = forms.EmailField(max_length=200, error_messages=messages)
    username = forms.CharField(error_messages=messages)
    first_name = forms.CharField(error_messages=messages)
    last_name = forms.CharField(error_messages=messages)
    phone_number = forms.CharField(error_messages=messages)
    national_code = forms.CharField(error_messages=messages)

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'national_code',"password")
