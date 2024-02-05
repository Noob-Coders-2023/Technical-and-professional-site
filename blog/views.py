from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContectForm, ChoicesForm, CourseForm
from .models import Course, Conect, Choes_cours
from django.contrib import messages
from gallery.models import Image
from posts.models import Post
import pandas as pd
from django.http import HttpResponse
from jdatetime import datetime
from datetime import date as datetimeen
from extension.utils import persian_number_converter
from persiantools.jdatetime import JalaliDate
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
import xlwt


# Create your views here.


def home(request):
    # course_list = Course.objects.filter(status='n').order_by('start')
    course_list = Course.objects.all().order_by('start')
    n = datetimeen.today()
    for o in course_list:
        if o.start > n:
            o.status = 'n'
        else:
            o.status = 'f'
    img_list = Image.objects.all()
    posts = Post.objects.all()
    paginator = Paginator(course_list, 3)
    page = request.GET.get('page')
    courses = paginator.get_page(page)
    current_date = persian_number_converter(str(datetime.now().strftime("%Y/%m/%d")))
    context = {
        "courses": courses,
        "img_list": img_list,
        'posts': posts,
        'current_date': current_date

    }
    return render(request, 'blog/home.html', context)


@login_required()
def detail(request, id):
    context = {
        "course": get_object_or_404(Course, id=id, status='n'),

    }
    selected = Choes_cours.objects.filter(user_id=request.user.id, id=context['course'].id)
    if selected.exists():
        context['selected'] = selected.get()

    if request.user.is_authenticated:

        return render(request, 'blog/detail.html', context)
    else:
        return redirect('account:login')
        if request.user.is_authenticated:
            return render(request, 'blog/detail.html', context)


def conect(request):
    if request.method == 'POST':
        form = ContectForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Conect.objects.create(title=cd['title'], text=cd['text'], user=request.user)
            messages.success(request, "پیام شما ارسال شد")
            return redirect('blog:conect')


    else:
        form = ContectForm()

    return render(request, 'blog/conect.html', {'form': form})


def choices(request):
    if request.method == 'POST':
        form = ChoicesForm(request.POST)

        if form.is_valid() or True:
            cd = form.cleaned_data
            Choes_cours.objects.create(cours_id=int(cd['course_id']), user_id=request.user.id)

            return redirect('blog:home')

        return redirect('blog:home')


def user_selected_courses(request):
    if request.user.is_authenticated:
        user_courses = Choes_cours.objects.filter(user=request.user)

        context = {
            'user_courses': user_courses,
            'selected': True
        }

        return render(request, 'registration/home.html', context)


def delete_course(request, id):
    user_courses = Choes_cours.objects.filter(id=id)

    if user_courses.exists():
        user_course = user_courses.first()
        user_course.delete()

    return redirect('blog:home')


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            # jalali_start = JalaliDate.to_jalali(form.cleaned_data['start'])
            # jalali_end = JalaliDate.to_jalali(form.cleaned_data['end'])
            # course = form.save(commit=False)
            # course.start = jalali_start.togregorian()
            # course.end = jalali_end.togregorian()
            form.save()
            messages.success(request, "کلاس شما ایجاد شد.")
            return redirect('blog:create_course')
        else:
            messages.error(request, "لطفا دوباره امتحان کنید. ")
    else:
        form = CourseForm()

    return render(request, 'blog/create_course.html', {'form': form})


from melipayamak import Api
import requests


def export_courses_to_excel(request):
    import requests

    data = {'from': '50002710017796', 'to': '09916450191', 'text': 'test sms'}
    response = requests.post('https://console.melipayamak.com/api/send/simple/e97f2fd3453d4717bd528e07a8210f0d',
                             json=data)
    print(response)


def export_courses_to_excel1(request):
    # خواندن لیست دروس از پایگاه داده
    courses = Choes_cours.objects.all()
    lst = []
    for o in courses:
        lst.append({
            'نام': o.user.first_name,
            'نام خانوادگی': o.user.last_name,
            'نام دوره': o.cours.title,

        })
    # تبدیل QuerySet به دیتافریم pandas
    # courses_df = pd.DataFrame(list(courses.values()))
    courses_df = pd.DataFrame(lst)

    # نام فایل Excel
    excel_file_name = 'registered_courses.xlsx'

    # تولید فایل Excel
    courses_df.to_excel(excel_file_name, index=False)

    # ارسال فایل Excel به عنوان پاسخ به درخواست
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{excel_file_name}"'
    courses_df.to_excel(response, index=False)

    return response
    # response=HttpResponse(content_type='application/ms-excel')
    # response['content-Disposition']='attachment;filename=student'+str(datetime..now())+'.xls'
    # workbook=xlwt.Workbook(encoding='utf-8')
    # worksheet=workbook.add_sheet('students')
    # columns=['name','last name','code']
    # rownumber=0
    # for col in range(len(columns)):
    #     worksheet.write(rownumber,col,columns[col])
    #
    #
    # students=Choes_cours.objects.all().values_list('course_id','user_id')
    # for std in students:
    #     rownumber+=1
    #     for col in range(len(std)):
    #         worksheet.write(rownumber,col,std[col])
    #
    # workbook.save(response)
    #
    # return response
