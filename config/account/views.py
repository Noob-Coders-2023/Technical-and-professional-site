# from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from blog.models import Choes_cours

from .forms import SignupForm
from .tokens import account_activation_token
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

from account.models import User
# Create your views here.




def home(request):
    return render(request,'registration/home.html')


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')





def user_selected_courses(request):
    if request.user.is_authenticated:
        user_courses = Choes_cours.objects.filter(user=request.user)

        context = {
            'user_courses': user_courses,
        }
        return render(request,'registration/home.html', context)

        # # اگر کاربر وارد نشده باشد، می‌توانید به صفحه ورود منتقل کنید یا هر عمل دیگری انجام دهید.
        # return render(request, 'not_authenticated.html')


class Register(CreateView):
    form_class=SignupForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعال سازی اکانت'
        message = render_to_string('registration/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': force_str(urlsafe_base64_encode(force_bytes(user.pk))),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('لینک فعال‌سازی به ایمیل شما ارسال شد ')




def activate(request, uidb64, token):
    context = {'uidb64': uidb64, 'token': token}

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        return render(request, 'registration/account_activation_email.html')
    else:
        return render(request, 'registration/account_activation_invalid.html')

    return render(request, 'registration/activate_account.html.html', context)

