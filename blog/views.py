from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import ContectForm, ChoicesForm, CourseForm
from .models import Course, Conect, Choes_cours
from django.contrib import messages
from gallery.models import Image


# Create your views here.


def home(request):
    course_list = Course.objects.filter(status='n').order_by('start')
    img_list = Image.objects.all()
    paginator = Paginator(course_list, 2)
    page = request.GET.get('page')
    courses = paginator.get_page(page)

    context = {
        "courses": courses,
        "img_list": img_list
    }
    return render(request, 'blog/home.html', context)


@login_required()
def detail(request, slug):
    context = {
        "course": get_object_or_404(Course, slug=slug, status='n'),

    }
    selected = Choes_cours.objects.filter(user_id=request.user.id, cours_id=context['course'].id)
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
            messages.success(request, "Message sent.")
            return redirect('blog:home')


    else:
        form = ContectForm()

    return render(request, 'blog/conect.html', {'form': form})
    messages.success(request, "Message sent.")


def choices(request):
    if request.method == 'POST':
        form = ChoicesForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            Choes_cours.objects.create(cours_id=int(cd['course_id']), user_id=request.user.id)

            return redirect('blog:home')


def user_selected_courses(request):
    if request.user.is_authenticated:
        user_courses = Choes_cours.objects.filter(user=request.user)

        context = {
            'user_courses': user_courses,
            'selected': True
        }

        return render(request, 'registration/home.html', context)


def delete_course(request, course_id):
    user_courses = Choes_cours.objects.filter(id=course_id)

    if user_courses.exists():
        user_course = user_courses.first()
        user_course.delete()

    return redirect('blog:home')


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = CourseForm()

    return render(request, 'blog/create_course.html', {'form': form})
