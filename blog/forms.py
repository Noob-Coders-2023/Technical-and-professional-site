from django import forms
from blog.models import Course,Choes_cours
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget


class ContectForm(forms.Form):
    messages = {
        "required": 'لطفا این فیلد را پر کنید',

    }
    first_lastname=forms.CharField(label='نام و نام خانوادگی', error_messages=messages)
    national_code=forms.CharField(label='کدملی', error_messages=messages)
    phone_number=forms.CharField(label='شماره تماس', error_messages=messages)
    title = forms.CharField(label='موضوع', error_messages=messages)
    text = forms.CharField(label='متن پیام', error_messages=messages)


class ChoicesForm(forms.Form):
    GENDER_CHOICES = (
        ('w', 'مونث'),
        ('m', 'مذکر'),

    )
    course_id=forms.CharField(label='موضوع')
    gender = forms.ChoiceField(label='جنسیت', choices=GENDER_CHOICES)


class CourseForm(forms.ModelForm):


    class Meta:
        model = Course
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super(CourseForm,self).__init__(*args,**kwargs)
        self.fields['start']=JalaliDateField(label=('تاریخ شروع'),widget=AdminJalaliDateWidget)
        self.fields['end']=JalaliDateField(label=('تاریخ پایان'),widget=AdminJalaliDateWidget)


