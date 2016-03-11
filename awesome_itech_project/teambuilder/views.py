from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from teambuilder.models import Team, Course
from teambuilder.forms import UserForm,TeamForm,CourseForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    teams = Team.objects.order_by('-creation_date')[:5]
    courses = Course.objects.order_by('add_date')[:5]
    context_dict = {}
    context_dict['teams'] = teams
    context_dict['courses'] = courses
    return render(request, 'teambuilder/index.html', context_dict)

def about(request):
    return render(request, 'teambuilder/about.html', {})

def register(request):

    context_dict = {}
    if request.method=='POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            context_dict['registered'] = True

        else:
            context_dict['errors'] = user_form.errors

    else:
        user_form = UserForm();
        context_dict['user_form'] = user_form

    return render(request, 'teambuilder/register.html', context_dict)

def reset_password(request):
    return render(request, 'teambuilder/reset_password.html', {})

def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/teambuilder/')

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

@login_required
def create_team(request):
    context_dict = {}
    if request.method=='POST':
        team_form = TeamForm(data=request.POST)

        if team_form.is_valid():
            user = request.user
            team = team_form.save(commit=False)
            team.creator = user
            team.save()
            context_dict['created'] = True

        else:
            context_dict['errors'] = team_form.errors

    else:
        team_form = TeamForm();
        context_dict['team_form'] = team_form
    return render(request, 'teambuilder/create_team.html', context_dict)

def profile(request):
    return render(request, 'teambuilder/profile.html', {})

def edit_profile(request):
    return render(request, 'teambuilder/edit_profile.html', {})

def team_details(request, team_name_slug):
    return render(request, 'teambuilder/team_detail.html', {"team_name":team_name_slug})

def find_team(request):
    return render(request, 'teambuilder/find_team.html', {})

def add_course(request):
    context_dic= {}
    if request.method=='POST':
        course_form=CourseForm(request.POST)

        if course_form.is_valid():
            course=course_form.save(commit=True)
           # course.creator=user
            course.save()
            context_dic['created']=True

            return (request)
        else:
            context_dic['errors']=course_form.errors
    else:
        course_form=CourseForm()
        context_dic['course_form']=course_form
    return render(request,'teambuilder/add_course.html',context_dic)


