from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'teambuilder/index.html', {})

def about(request):
    return render(request, 'teambuilder/about.html', {})

def register(request):
    return render(request, 'teambuilder/register.html', {})

def reset_password(request):
    return render(request, 'teambuilder/reset_password.html', {})

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request,user)
            return HttpResponseRedirect('/teambuilder/')

        else:
            return render(request, 'teambuilder/login.html', {'message':'Invalid username/password provided'})
    else:
        return render(request, 'teambuilder/login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/teambuilder/')

def create_team(request):
    return render(request, 'teambuilder/create_team.html', {})

def profile(request):
    return render(request, 'teambuilder/profile.html', {})

def edit_profile(request):
    return render(request, 'teambuilder/edit_profile.html', {})

def team_details(request, team_name_slug):
    return render(request, 'teambuilder/team_detail.html', {"team_name":team_name_slug})

def find_team(request):
    return render(request, 'teambuilder/find_team.html', {})
