from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'teambuilder/index.html', {})

def register(request):
    return render(request, 'teambuilder/register.html', {})

def reset_password(request):
    return render(request, 'teambuilder/reset_password.html', {})

def login(request):
    return render(request, 'teambuilder/login.html', {})

def create_team(request):
    return render(request, 'teambuilder/create-team.html', {})

def profile(request):
    return render(request, 'teambuilder/profile.html', {})

def edit_profile(request):
    return render(request, 'teambuilder/edit_profile.html', {})

def team_details(request, team_name_slug):
    return render(request, 'teambuilder/team_detail.html', {})

def find_team(request):
    return render(request, 'teambuilder/find_team.html', {})
