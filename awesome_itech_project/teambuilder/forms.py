from django import forms
from django.contrib.auth.models import User
from models import Team,Course
from models import Team, Course


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

class TeamForm(forms.ModelForm):
    course_password = forms.CharField(max_length=15, required=True)

    class Meta:
        model = Team
        fields = ('name', 'course', 'required_skills','description')

class CourseForm(forms.ModelForm):
    #code=forms.CharField(max_length=15, help_text="Please enter the course code")
    #name=forms.CharField(max_length=100, help_text="Please enter the course name")
    #course_password=forms.CharField(max_length=15, help_text="Please enter the course password")
    #team_size=forms.IntegerField(help_text="Please enter the team size")
   ## likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    #widget=IntegerField()


    class Meta:
        model = Course
        fields = ('code','name','course_password','team_size',)

