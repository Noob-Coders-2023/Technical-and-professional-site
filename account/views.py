from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from course.models import Choes_cours
from .forms import SignupForm, CustomUserChangeForm, VerifyCodeForm, CaptchaAuthenticationForm
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
from account.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.views import APIView
from . import serliazers
from django.views import View
import random
from utils import send_top_code
from .models import OtpCode
from django.contrib import messages
from jdatetime import datetime
from extension.utils import persian_number_converter
from django.contrib.auth.views import LoginView
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
CustomUser = get_user_model()
# Create your views here.


class CustomLoginView(LoginView):
    form_class = CaptchaAuthenticationForm

@ratelimit(key='user_or_ip', rate='10/m')
def home(request):
    return render(request, 'registration/home.html')


class PasswordChange(PasswordChangeView):
    @method_decorator(ratelimit(key='user_or_ip', rate='1/s'))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success_url = reverse_lazy('account:password_change_done')

@ratelimit(key='user_or_ip', rate='10/m')
def user_selected_courses(request):
    if request.user.is_authenticated:
        user_courses = Choes_cours.objects.filter(user=request.user)

        context = {
            'user_courses': user_courses,
        }

        return render(request, 'registration/home.html', context)


class Register(View):

    form_class = SignupForm

    @method_decorator(ratelimit(key='user_or_ip', rate='1/s'))
    def get(self, request):
        form = self.form_class
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            random_code = random.randint(1000, 9999)
            send_top_code(form.cleaned_data['phone_number'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'username': form.cleaned_data['username'],
                'password2': form.cleaned_data['password2'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'national_code': form.cleaned_data['national_code'],
                'gender': form.cleaned_data['gender'],


            }
            messages.success(request, 'کدی برای شما ارسال شد', 'success')
            return redirect('account:verify_code')
        messages.error(request, 'فیلد ها صحیح وارد نشده اند.', 'error')
        return render(request, 'registration/register.html', {"form": form})


# def activate(request, uidb64, token):
#     context = {'uidb64': uidb64, 'token': token}
#
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         # login(request, user)
#         # return redirect('home')
#         return render(request, 'registration/account_activation_email.html')
#     else:
#         return render(request, 'registration/account_activation_invalid.html')
#
#     return render(request, 'registration/activate_account.html', context)


class UserRegisterVerifyCodeView(View):

    form_class = VerifyCodeForm
    @method_decorator(ratelimit(key='user_or_ip', rate='1/s'))
    def get(self, request):
        form = self.form_class
        return render(request, 'registration/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'],
                                         user_session['username'], user_session['password2'],
                                         user_session['first_name'],
                                         user_session['last_name'], user_session['national_code']
                                         , user_session['gender'])

                code_instance.delete()
                messages.success(request, 'ثبت نام شما با موفقیت انجام شد', 'success')
            else:
                messages.error(request, 'کد شما اشتباه است', 'danger')
                return redirect('account:verify_code')
        return redirect('course:home')


@login_required
@ratelimit(key='user_or_ip', rate='10/m')
def profile(request):
    current_date = persian_number_converter(str(datetime.now().strftime("%Y/%m/%d")))
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات با موفقیت ذخیره شدند.', 'success')
            return redirect('account:profile')

        else:
            messages.error(request, 'لطفاً اطلاعات را به درستی وارد کنید.')
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form': form,
        'current_date': current_date
    }

    return render(request, 'registration/profile.html',context)






