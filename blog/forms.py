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
        fields = ['first_lastname', 'national_code', 'phone_number', 'title', 'text', 'mehvar', 'subject']
        widgets = {'mehvar': forms.CheckboxSelectMultiple()}

    MEHVAR_CHOICES = [
        ('ma', 'مالی'),
        ('ed', 'اداری'),
        ('am', 'آموزش'),
        ('sa', 'سنجش و گواهینامه'),
        ('ta', 'تکریم ارباب رجوع'),
    ]
    SUBJECT_CHOICES =(
        ('sh','شکایت'),
        ('da','درخوایت'),
        ('en','انتقاد'),

    )

    first_lastname = forms.CharField(label='نام و نام خانوادگی', error_messages=messages)
    national_code = forms.CharField(label='کدملی', error_messages=messages)
    phone_number = forms.CharField(label='شماره تماس', error_messages=messages)
    title = forms.CharField(label='موضوع', error_messages=messages)
    text = forms.CharField(label='متن پیام', error_messages=messages)
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

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['start'] = JalaliDateField(label=('تاریخ شروع'), widget=AdminJalaliDateWidget)
        self.fields['end'] = JalaliDateField(label=('تاریخ پایان'), widget=AdminJalaliDateWidget)
