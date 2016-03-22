from django import forms
from django.contrib.auth.models import User
from models import Team,Course,UserProfile
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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'about_me', 'role')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('code', 'name', 'course_password', 'team_size',)

