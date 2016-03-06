from django import forms
from django.contrib.auth.models import User
from models import Team

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

    class Meta:
        model = Team
        fields = ('name', 'course','current_size', 'required_skills','description')


