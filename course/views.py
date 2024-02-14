from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContectForm, ChoicesForm, CourseForm
from .models import Course, Conect, Choes_cours, Free_school
from django.contrib import messages
from gallery.models import Image
from posts.models import Post
import pandas as pd
from django.http import HttpResponse
from jdatetime import datetime
from extension.utils import persian_number_converter
from datetime import date as datetimeen


# Create your views here.

# ----------------page home
def home(request):
    course_list = Course.objects.all().order_by('status')
    n = datetimeen.today()
    for o in course_list:
        if o.start > n:
            o.status = 'n'
        else:
            o.status = 'f'
    img_list = Image.objects.all()
    posts = Post.objects.all()
    paginator = Paginator(course_list, 8)
    page = request.GET.get('page')
    courses = paginator.get_page(page)
    current_date = persian_number_converter(str(datetime.now().strftime("%Y/%m/%d")))
    context = {
        "courses": courses,
        "img_list": img_list,
        'posts': posts,
        'current_date': current_date

    }
    return render(request, 'course/home.html', context)


# --------------detail cours
@login_required()
def detail(request, id):
    current_date = persian_number_converter(str(datetime.now().strftime("%Y/%m/%d")))
    context = {
        "course": get_object_or_404(Course, id=id, status='n'),
        'current_date': current_date
    }
    selected = Choes_cours.objects.filter(user_id=request.user.id, cours_id=context['course'].id)
    if selected.exists():
        context['selected'] = selected.get()

    if request.user.is_authenticated:
        return render(request, 'course/detail.html', context)

    return redirect('account:login')


# --------ارتباط با مسولین---------
def conect(request):
    if request.method == 'POST':
        form = ContectForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            national_code = form.cleaned_data.get('national_code')
            user_national_code = request.user.national_code
            user_phone_number = request.user.phone_number

            if phone_number != user_phone_number:
                form.add_error('phone_number', 'شماره تلفن وارد شده باید با شماره تلفن ثبت نام شما مطابقت داشته باشد.')
                return render(request, 'course/conect.html', {'form': form})
            if national_code != user_national_code:
                form.add_error('national_code', 'کد ملی وارد شده باید با کد ملی ثبت نام شما مطابقت داشته باشد.')
                return render(request, 'course/conect.html', {'form': form})
            cd = form.cleaned_data
            Conect.objects.create(title=cd['title'], text=cd['text'], first_lastname=cd['first_lastname'],relationship=cd['relationship'],
                                  user=request.user)
            messages.success(request, "پیام شما ارسال شد")
            return redirect('course:conect')

        else:
            messages.error(request, "پیام شما ارسال نشد,لطفا دوباره امتحان کنید.")

            return render(request, 'course/conect.html', {'form': form})


    else:
        form = ContectForm()

    return render(request, 'course/conect.html', {'form': form})


# _____________form shekayat ___________
def complaint(request):
    if request.method == 'POST':
        form = complaint(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            national_code = form.cleaned_data.get('national_code')
            user_national_code = request.user.national_code
            user_phone_number = request.user.phone_number

            if phone_number != user_phone_number:
                form.add_error('phone_number', 'شماره تلفن وارد شده باید با شماره تلفن ثبت نام شما مطابقت داشته باشد.')
                return render(request, 'course/complaint_form.html', {'form': form})
            if national_code != user_national_code:
                form.add_error('national_code', 'کد ملی وارد شده باید با کد ملی ثبت نام شما مطابقت داشته باشد.')
                return render(request, 'course/complaint_form.html', {'form': form})
            cd = form.cleaned_data
            Conect.objects.create(title=cd['title'], text=cd['text'], user=request.user, first_lastname=cd['first_lastname'],subject=cd['subject'],
                                  mehvar=cd['mehvar']
                                  )
            messages.success(request, "پیام شما ارسال شد")
            return redirect('course:complaint')

        else:
            messages.error(request, "پیام شما ارسال نشد,لطفا دوباره امتحان کنید.")

            return render(request, 'course/complaint_form.html', {'form': form})


    else:
        form = ContectForm()

    return render(request, 'course/complaint_form.html', {'form': form})


def choices(request):
    if request.method == 'POST':
        form = ChoicesForm(request.POST)

        if form.is_valid() or True:
            cd = form.cleaned_data
            Choes_cours.objects.create(cours_id=int(cd['course_id']), user_id=request.user.id)

            return redirect('course:home')

        return redirect('course:home')


def user_selected_courses(request):
    if request.user.is_authenticated:
        user_courses = Choes_cours.objects.filter(user=request.user)

        context = {
            'user_courses': user_courses,
            'selected': True
        }

        return render(request, 'registration/home.html', context)


# ------حذف درس----------
def delete_course(request, id):
    user_courses = Choes_cours.objects.filter(id=id)

    if user_courses.exists():
        user_course = user_courses.first()
        user_course.delete()

    return redirect('course:home')


# -----ساخت درس توسط ادمین----------
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            start_time = form.cleaned_data['start']
            end_time = form.cleaned_data['end']

            if end_time <= start_time:
                messages.error(request, "زمان پایان دوره باید بعد از زمان شروع باشد.")
            else:
                form.save()
                messages.success(request, "کلاس شما ایجاد شد.")
                return redirect('course:create_course')
        else:
            messages.error(request, "لطفا دوباره امتحان کنید. ")
    else:
        form = CourseForm()

    return render(request, 'course/create_course.html', {'form': form})


# ------دریافت لیست دروس اتخابی کلاینت---
def export_courses_to_excel(request):
    courses = Choes_cours.objects.all()

    if not courses:
        return HttpResponse("هیچ دوره‌ای برای صدور یافت نشد.")

    lst = []
    for o in courses:
        jalali_selection_time = datetime.fromgregorian(datetime=o.selection_time).strftime('%Y/%m/%d')
        lst.append({
            'ردیف': len(lst) + 1,
            'نام': o.user.username,
            'نام خانوادگی': o.user.last_name,
            'کدملی': o.user.national_code,
            'شماره تماس': o.user.phone_number,
            'نام دوره': o.cours.title,
            'زمان انتخاب': jalali_selection_time,

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
# ------دریافت لیست تمامی دروس ---
def all_courses_to_excel(request):
    courses = Course.objects.all()

    if not courses:
        return HttpResponse("هیچ دوره‌ای برای صدور یافت نشد.")

    lst = []
    for o in courses:
        jalali_start = datetime.fromgregorian(datetime=o.start).strftime('%Y/%m/%d')
        jalali_end = datetime.fromgregorian(datetime=o.end).strftime('%Y/%m/%d')
        gender_display = 'زن' if o.gender == 'w' else 'مرد' if o.gender == 'm' else 'زن و مرد'
        lst.append({
            'ردیف': len(lst) + 1,
            'نام دوره': o.title,
            'مدرس': o.teacher,
            'کد درس': o.course_code,
            'تاریخ شروع':jalali_start,
            'تاریخ پایان': jalali_end,
            'نام مرکز دولتی': o.govermentcenter,
            'کارگاه/آموزشگاه': o.workshop,
            'جنسیت': gender_display,

        })

    courses_df = pd.DataFrame(lst)


    excel_file_name = 'all_courses.xlsx'

    # تولید فایل Excel
    courses_df.to_excel(excel_file_name, index=False)

    # ارسال فایل Excel به عنوان پاسخ به درخواست
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{excel_file_name}"'
    courses_df.to_excel(response, index=False)

    return response



# ---------لیست اموزشگاه های آزاد----------
def free_school(request):
    academy_list = Free_school.objects.all()
    context = {
        'academy_list': academy_list
    }
    return render(request, 'access/free_school.html', context)
