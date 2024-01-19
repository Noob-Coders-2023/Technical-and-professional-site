from django import forms
from blog.models import Course
from django.forms.renderers import TemplatesSetting



class ContectForm(forms.Form):
    messages = {
        "required":'لطفا این فیلد را پر کنید',


    }
    title=forms.CharField(label= 'موضوع',error_messages=messages)

    text=forms.CharField(widget=forms.Textarea,label='متن پیام')
class ChoicesForm(forms.Form):
    course_id=forms.CharField(label='موضوع')



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


