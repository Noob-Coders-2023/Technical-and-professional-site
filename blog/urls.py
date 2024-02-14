from django.urls import path
from .views import *

app_name = "blog"
urlpatterns = [
    path('', home, name='home'),
    path('course/<int:id>', detail, name='detail'),
    path('conect/', conect, name='conect'),
    path('choices/', choices, name='choices'),
    path('create_course/', create_course, name='create_course'),
    path('delete_course/<int:id>/', delete_course, name='delete_course'),
    path('export-courses/', export_courses_to_excel, name='export_courses_to_excel'),
    path('amozeshgayeazad/',free_school, name='free_school'),
    path('complaint_form/',complaint, name='complaint'),

]
