from django import forms
from blog.models import Course,Choes_cours
from django.forms.renderers import TemplatesSetting


class ContectForm(forms.Form):
    messages = {
        "required": 'لطفا این فیلد را پر کنید',

    }
    title = forms.CharField(label='موضوع', error_messages=messages)

    text = forms.CharField(widget=forms.Textarea, label='متن پیام')


class ChoicesForm(forms.Form):
    GENDER_CHOICES = (
        ('w', 'مونث'),
        ('m', 'مذکر'),

    )
    course_id=forms.CharField(label='موضوع')
    gender = forms.ChoiceField(label='جنسیت', choices=GENDER_CHOICES, required=True)


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
