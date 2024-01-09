from django import forms
from blog.models import Course
from django.forms.renderers import TemplatesSetting




class ContectForm(forms.Form):
    title=forms.CharField(label='موضوع')

    text=forms.CharField(widget=forms.Textarea,label='متن پیام')
class ChoicesForm(forms.Form):
    course_id=forms.CharField(label='موضوع')



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


