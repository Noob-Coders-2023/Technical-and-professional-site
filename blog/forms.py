from django import forms
from blog.models import Course, Conect
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget


class ContectForm(forms.ModelForm):
    messages = {
        "required": 'لطفا این فیلد را پر کنید',
    }

    class Meta:
        model = Conect
        exclude = [ 'subject', 'mehvar']
        fields = ['first_lastname', 'national_code', 'phone_number', 'title', 'text', 'relationship']


    RELATIONSHIP_CHOICES = (
        ('rm', 'رییس مرکز'),
        ('ka', 'کارشناس آموزش'),
        ('ki', 'کارشناس it'),
        ('ma', 'معاون آموزش'),
        ('em', 'ارتباط با مربیان'),
    )
    first_lastname = forms.CharField(label='نام و نام خانوادگی', error_messages=messages)
    national_code = forms.CharField(label='کدملی', error_messages=messages)
    phone_number = forms.CharField(label='شماره تماس', error_messages=messages)
    title = forms.CharField(label='موضوع', error_messages=messages)
    text = forms.CharField(label='متن پیام', error_messages=messages, widget=forms.Textarea)
    relationship = forms.ChoiceField(label='ارتباط با', error_messages=messages, choices=RELATIONSHIP_CHOICES)


#   فرم شکایت---------------------------
class complaint (forms.ModelForm):
    messages = {
        "required": 'لطفا این فیلد را پر کنید',
    }
    SUBJECT_CHOICES = (
        ('sh', 'شکایت'),
        ('da', 'درخواست'),
        ('en', 'انتقاد'),

    )
    MEHVAR_CHOICES = (
        ('ma', 'مالی'),
        ('ed', 'اداری'),
        ('am', 'آموزش'),
        ('sa', 'سنجش و گواهینامه'),
        ('ta', 'تکریم ارباب رجوع'),

    )
    class Meta:
        model = Conect
        exclude = [ 'relationship']
        fields = ['first_lastname', 'national_code', 'phone_number', 'title', 'text', 'mehvar', 'subject']
        widgets = {'mehvar': forms.CheckboxSelectMultiple()}

    first_lastname = forms.CharField(label='نام و نام خانوادگی', error_messages=messages)
    national_code = forms.CharField(label='کدملی', error_messages=messages)
    phone_number = forms.CharField(label='شماره تماس', error_messages=messages)
    title = forms.CharField(label='موضوع', error_messages=messages)
    text = forms.CharField(label='متن پیام', error_messages=messages, widget=forms.Textarea)
    mehvar = forms.MultipleChoiceField(label='محور شکایت', choices=MEHVAR_CHOICES, widget=forms.CheckboxSelectMultiple)
    subject = forms.ChoiceField(label='موضوع', error_messages=messages, choices=SUBJECT_CHOICES)

class ChoicesForm(forms.Form):
    GENDER_CHOICES = (
        ('w', 'مونث'),
        ('m', 'مذکر'),

    )
    course_id = forms.CharField(label='موضوع')
    gender = forms.ChoiceField(label='جنسیت', choices=GENDER_CHOICES)


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    description = forms.CharField(max_length=700, widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['start'] = JalaliDateField(label=('تاریخ شروع'), widget=AdminJalaliDateWidget)
        self.fields['end'] = JalaliDateField(label=('تاریخ پایان'), widget=AdminJalaliDateWidget)
