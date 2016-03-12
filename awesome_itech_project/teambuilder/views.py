from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from teambuilder.models import Team, Course, Memberrequest
from teambuilder.forms import UserForm,TeamForm
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
            team.name = team.name.title()
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

    context_dict = {}
    try:
        team = Team.objects.get(slug=team_name_slug)
        context_dict['team'] = team
        available_slots = team.course.team_size - team.current_size
        context_dict['available_slots'] = available_slots

        #check if user has previously requested to join the team
        user = request.user
        if user.is_authenticated():
            try:
                mr = Memberrequest.objects.get(team=team,user=user)
                context_dict['member_request'] = mr

            except Memberrequest.DoesNotExist:
                pass


    except Team.DoesNotExist:
        pass

    return render(request, 'teambuilder/team_detail.html', context_dict)
    #return render(request, 'teambuilder/team_detail.html', {"team_name":team_name_slug})

def find_team(request):
    return render(request, 'teambuilder/find_team.html', {})

@login_required
def join_team(request, team_name_slug):
    user = request.user
    team = Team.objects.get(slug=team_name_slug)
    mr = Memberrequest.objects.get_or_create(user=user,team=team)
    return_string = "Your request to join {0} has been sent".format(team_name_slug)
    return HttpResponse(return_string)

def cancel_request(request):

    return render
