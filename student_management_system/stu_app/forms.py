from django import forms
from .models import Student

gender_choices = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER')
]

subjects_choices = [
    ('PHYSICS','PHYSICS'),
    ('IT','IT'),
    ('CHEMISTRY','CHEMISTRY'),
    ('BIOLOGY','BIOLOGY'),
    ('CS','CS'),
]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'roll':'STUDENT ROLL',
            'first_name':'FIRST NAME',
            'last_name':'LAST NAME',
            'age':'AGE',
            'city':'CITY',
            'gender':'GENDER',
            'mobile_no':'MOBILE NO',
            'subjects':'SUBJECTS',
            'email':'EMAIL ID',
            'password':'PASSWORD',
            'eligible':'ELIGIBILITY',
        }   
        widgets = {
            'roll':forms.TextInput(attrs={
                'placeholder':'E.g.,101',
                'required':True,
            }),
            'first_name':forms.TextInput(attrs={
                'placeholder':'Enter First Name',
                'required':True
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Enter Last Name'
            }),
            'city':forms.TextInput(attrs={
                'placeholder':'Enter city',
            }),
            'email':forms.TextInput(attrs={
                'placeholder':'youremail@gmail.com',
                'required':True
            }),
            'password':forms.PasswordInput(attrs={
                'placeholder':'********',
                'required':True,
                'type':'password'
            }),
            'gender':forms.RadioSelect(choices=gender_choices),
            'subjects':forms.Select(choices=subjects_choices)
        }
