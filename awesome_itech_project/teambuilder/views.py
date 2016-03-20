from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from teambuilder.forms import UserForm,TeamForm,CourseForm
from teambuilder.models import Team, Course, Memberrequest,UserProfile,User
from teambuilder.forms import UserForm,TeamForm,ProfileForm
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.
def index(request):
    teams = Team.objects.filter(status=True).order_by('-creation_date')[:5]
    courses = Course.objects.order_by('-add_date')[:5]
    context_dict = {}
    context_dict['teams'] = teams
    context_dict['courses'] = courses
    return render(request, 'teambuilder/index.html', context_dict)


def about(request):
    return render(request, 'teambuilder/about.html', {})


@login_required
def create_team(request):
    context_dict = {}
    if request.method=='POST':
        team_form = TeamForm(data=request.POST)
        context_dict['team_form'] = team_form
        if team_form.is_valid():
            course_password = request.POST['course_password']
            course_id = request.POST['course']
            course = Course.objects.get(pk=course_id)

            if course_password == course.course_password:
                team = team_form.save(commit=False)
                team.creator = request.user
                created_before = Team.objects.filter(course=course, creator=team.creator, status = True) #check if user has created an active team for the course previously

                if len(created_before) > 0:
                    context_dict['error'] = "You have already created a team for this course before"
                else:
                    team.name = team.name.title()
                    team.save()
                    context_dict['created'] = True
                    return HttpResponseRedirect('/teambuilder/team/'+team.slug+'/')

            else:
                context_dict['error'] = "Invalid course password provided"
                context_dict['created'] = False

        else:
            context_dict['errors'] = team_form.errors

    else:
        team_form = TeamForm();
        context_dict['team_form'] = team_form
    return render(request, 'teambuilder/create_team.html', context_dict)

@login_required
def profile(request, username):
    context_dict = {}
    try:
        u = User.objects.get(username=username)
        up = UserProfile.objects.get(user=u)

        context_dict['profile']=up

    except User.DoesNotExist:
        return HttpResponseRedirect('/teambuilder/page-not-found/')
    except UserProfile.DoesNotExist:
        return HttpResponseRedirect('/teambuilder/page-not-found/')

    return render(request, 'teambuilder/profile.html', context_dict)


def edit_profile(request):
    context_dict = {}
    user = request.user
    profile2 = UserProfile.objects.get(user=user)
    if request.method=='POST':

        profile_form = ProfileForm(data=request.POST, instance=profile2)

        # use a UserProfile object to store data collected
        dob2 = datetime.strptime(request.POST['dob'], "%Y-%m-%d").date()
        uprofile = UserProfile(dob=dob2, about_me=request.POST['about_me'],
                               phone_number=request.POST['phone_number'], user=request.user)

        # check the user profile part for validity
        if profile_form.is_valid():
            # if form is valid, save
            # save the user details part
            user.first_name=request.POST['first_name']
            user.last_name=request.POST['last_name']
            user.save()

            user_profile = profile_form.save(commit=False)
            if 'picture' in request.FILES:
                user_profile.picture = request.FILES['picture']
            user_profile.save()
            context_dict['created'] = True
        else:
            # else show errors
            context_dict['errors'] = profile_form.errors
            context_dict['profile'] = uprofile  # pass already entered data back to the user
    else:
        context_dict['profile'] = profile2
    return render(request, 'teambuilder/edit_profile.html', context_dict)


def team_details(request, team_name_slug):

    context_dict = {}
    try:
        team = Team.objects.get(slug=team_name_slug)
        context_dict['team'] = team

        #check if user has previously requested to join the team
        user = request.user
        if user.is_authenticated():
            try:
                mr = Memberrequest.objects.get(team=team,user=user,status="pending")
                context_dict['member_request'] = mr

            except Memberrequest.DoesNotExist:
                pass

            #check if user has an already accepted request for that team
            try:
                mr2 = Memberrequest.objects.get(team=team,user=user,status="accepted")
                if mr2:
                    context_dict['accepted_request'] = True

            except Memberrequest.DoesNotExist:
                pass

    except Team.DoesNotExist:
        return HttpResponseRedirect('/teambuilder/page-not-found/')

    return render(request, 'teambuilder/team_detail.html', context_dict)


def find_team(request):
        team_list = []
        starts_with = ''
        if request.method == 'GET':
                starts_with = request.GET['suggestion']
        team_list = get_team_list(20, starts_with)

        return render(request, 'teambuilder/find_team.html', {'team_list': team_list })


def get_team_list(max_results=0, starts_with=''):
        team_list = None
        team_list1 = None
        course_list = None
        if starts_with:
                team_list = Team.objects.filter(name__istartswith=starts_with)
                course_list = Course.objects.filter(name__istartswith=starts_with)
                for course in course_list:
                        if team_list:
                            team_list1=Team.objects.filter(course=course)
                            for team in team_list1:
                               team_list.append(team)
                        else:
                               team_list = Team.objects.filter(course=course)

        else:
            team_list=Team.objects.all()
        if max_results > 0:
                if team_list.count() > max_results:
                        team_list = team_list[:max_results]

        return team_list


def search_team(request):
        team_list=[]
        team_list=Team.objects.all()
        return render(request, 'teambuilder/search_team.html', {'team_list': team_list })


@login_required
def add_course(request):
    context_dic = {}
    if request.method == 'POST': # user is sending data
        course_form = CourseForm(request.POST) # create form instance with submitted data

        # if form is valid, create a new Model instance of course and save it
        if course_form.is_valid():
            course = course_form.save(commit=False)
            course.creator = request.user
            course.save()
            context_dic['created'] = True

        # else form has errors. Add those errors to the context dictionary for rendering on the template file
        else:
            context_dic['errors']=course_form.errors

    # user is requesting data. Create and send back an empty form
    else:
        course_form=CourseForm()
        context_dic['course_form']=course_form
    return render(request,'teambuilder/add_course.html',context_dic)


@login_required
def join_team(request, team_name_slug):
    user = request.user
    team = Team.objects.get(slug=team_name_slug)
    Memberrequest.objects.get_or_create(user=user, team=team, status="pending")

    return HttpResponseRedirect('/teambuilder/team/'+team_name_slug+'/')


@login_required
def edit_team(request,team_name_slug):
    context_dict = {}
    try:
        user = request.user #get logged in user
        team = Team.objects.get(slug=team_name_slug) #get the specified team
        if request.method=='POST':
                team.name=request.POST['name']
                team.required_skills=request.POST['skill']
                team.description=request.POST['description']

                #update team with new details and save
                team.save()
                context_dict['created'] = True
        context_dict['user']=user
        context_dict['team']=team

    except Team.DoesNotExist: #redirect user to 404 page if team does not exist
        return HttpResponseRedirect('/teambuilder/page-not-found/')

    return render(request, 'teambuilder/edit_team.html', context_dict)


@login_required
def cancel_request(request, team_name_slug):
    user = request.user
    team = Team.objects.get(slug=team_name_slug)
    mr = Memberrequest.objects.get(user=user, team=team, status="pending")
    mr.status = "cancelled"
    mr.save()

    return HttpResponseRedirect('/teambuilder/team/'+team_name_slug+'/')


@login_required
def view_requests(request, team_name_slug):
    user = request.user
    team = Team.objects.get(slug=team_name_slug)

    if team.creator == user:
        requests = Memberrequest.objects.filter(team=team).order_by('-request_date')

        return render(request, 'teambuilder/view_requests.html', {'requests': requests, 'team': team})

    else:
        return HttpResponseRedirect('/teambuilder/unauthorized/')


@login_required
def accept_request(request, request_id):
    try:
        mr = Memberrequest.objects.get(pk=request_id)
        team = mr.team

        user = request.user
        if user == team.creator:
            if mr.status == "pending":
                mr.status = "accepted"
                team.current_size += 1
                team.save()
                mr.save()

                #reject any other pending requests for that team once the team size is full
                if team.current_size == team.course.team_size:
                    Memberrequest.objects.filter(team=team, status="pending").update(status="rejected")

                #cancel any other requests sent by a user to join other teams in the same course
                sender = mr.user
                reqs =  Memberrequest.objects.filter(user=sender, status='pending') #get the memberrequests sent by sender that are pending

                #select the ones with the same course and cancel them
                teams = team.course.team_set.all()
                for req in reqs:
                    if req.team in teams:
                        req.status = "cancelled"
                        req.save()


        else:
            return HttpResponseRedirect('/teambuilder/unauthorized/')

    except Memberrequest.DoesNotExist:
        return HttpResponseRedirect('/teambuilder/page-not-found/')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def reject_request(request, request_id):
    try:
        mr = Memberrequest.objects.get(pk=request_id)
        team = mr.team

        if request.user == team.creator:
            mr.status = "rejected"
            mr.save()

        else:
            return HttpResponseRedirect('/teambuilder/unauthorized/')

    except Memberrequest.DoesNotExist:
        return HttpResponseRedirect('/teambuilder/page-not-found/')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def view_team_members(request, team_name_slug):
    user = request.user
    context_dict = {}
    try:
        team = Team.objects.get(slug=team_name_slug)
        if team.creator == user or team.course.creator == user:
            requests = Memberrequest.objects.filter(team=team,status="accepted")
            context_dict['requests'] = requests
            context_dict['team_creator'] = team.creator
            context_dict['team'] = team

    except Team.DoesNotExist:
        return HttpResponseRedirect('/teambuilder/page-not-found/')

    return render(request, 'teambuilder/view_team_members.html', context_dict)


@login_required
def dashboard(request):
    user = request.user
    context_dict = {}
    context_list = []
    mrs = Memberrequest.objects.filter(user=user).order_by('-request_date')
    context_dict['requests2'] = mrs
    courses = Course.objects.filter(creator=user)
    context_dict['courses'] = courses

    #teams created by user
    teams = Team.objects.filter(creator=user)
    context_dict['teams'] = teams

    #request to teams sent by user that have been accepted
    reqs = Memberrequest.objects.filter(user=request.user, status="accepted")
    context_dict['requests'] = reqs
    teams = Team.objects.filter(creator=request.user, status=True)
    for team in teams:
        requests = Memberrequest.objects.filter(team=team).order_by('-request_date')
        context_list.append(requests)
    context_dict['requests3'] = context_list
    return render(request, 'teambuilder/dashboard.html', context_dict)


def course_details(request, course_name_slug):
    context_dict = {}
    try:
        course = Course.objects.get(slug=course_name_slug)
        context_dict['course'] = course
        if request.user.is_authenticated():
            if request.user == course.creator:
                context_dict['creator'] = True

    except Course.DoesNotExist:
        return HttpResponseRedirect('/teambuilder/page-not-found/')

    return render(request, 'teambuilder/course_detail.html', context_dict)


@login_required
def edit_course(request, course_name_slug):
    context_dict = {}
    try:
        old_course = Course.objects.get(slug=course_name_slug) # get course details
        if request.user == old_course.creator: # check if the user trying to edit is the course creator
            context_dict['course'] = old_course

            if request.method == 'POST':
                course_form = CourseForm(data=request.POST, instance=old_course)
                if course_form.is_valid():
                    course=course_form.save()
                    return HttpResponseRedirect('/teambuilder/course/'+course.slug+'/')
                else:
                    context_dict['errors']=course_form.errors

            else:
                pass

            return render(request,'teambuilder/edit_course.html',context_dict)

        else: # if user is not course creator, redirect to 403 page
            return HttpResponseRedirect('/teambuilder/unauthorized/')

    except Course.DoesNotExist: # if course does not exist, redirect to 404 page
        return HttpResponseRedirect('/teambuilder/page-not-found/')


def unauthorized(request):
    return render(request, 'teambuilder/403.html', {})


def page_not_found(request):
    return render(request, 'teambuilder/404.html', {})


@login_required
def view_course_teams(request, course_name_slug):
    context_dict = {}
    try:
        course = Course.objects.get(slug=course_name_slug)
        context_dict['course'] = course
        if course.creator == request.user:
            teams = Team.objects.filter(course=course)
            context_dict['teams'] =  teams

        else:
            return HttpResponseRedirect('/teambuilder/unauthorized/')

    except Course.DoesNotExist:
        return HttpResponseRedirect('/teambuilder/page-not-found/')
    except Team.DoesNotExist:
        return HttpResponseRedirect('/teambuilder/page-not-found/')

    return render(request, 'teambuilder/view_course_teams.html', context_dict)


@login_required
def merge_teams(request, course_name_slug):
    context_dict = {}
    course = None
    try:
            course = Course.objects.get(slug=course_name_slug)
            teams = Team.objects.filter(course=course,current_size__lt = course.team_size, status = True).order_by('name')
            context_dict['teams'] = teams
            context_dict['course'] = course

    except Course.DoesNotExist:
        return HttpResponseRedirect('/teambuilder/page-not-found/')

    #ensure that only the course creator can perform this operation
    if course.creator != request.user:
        return HttpResponseRedirect('/teambuilder/unauthorized/')

    if request.method == 'POST':
        parent_team_id = request.POST['team_1']
        child_team_id = request.POST['team_2']

        #check if user selected to merge a team with itself
        if parent_team_id == child_team_id:
            context_dict['message'] = "You cannot merge a team with itself"

        else:
            parent_team = Team.objects.get(pk=parent_team_id)
            child_team = Team.objects.get(pk=child_team_id)

            if parent_team.current_size + child_team.current_size > course.team_size:
                context_dict['message'] = "The teams could not be merged because their combined size exceeds the maximum team size for the course"
                context_dict['merge'] = False
            else:
                #deactivate the child_team and set its merge_with field to parent_team
                child_team.status = False
                child_team.merge_with = parent_team
                child_team.save()

                #move members from child team to parent team
                Memberrequest.objects.filter(team=child_team,status='accepted').update(team=parent_team)

                #create and auto-accept request for team creator of child team as it did not exist before
                Memberrequest(user=child_team.creator, status='accepted', team=parent_team).save()

                #reject all pending requests sent to child team
                Memberrequest.objects.filter(team=child_team,status="pending").update(status="rejected")

                #update current size of parent team
                parent_team.current_size += child_team.current_size
                parent_team.save()

                #if after merging the parent team becomes full, reject all pending requests sent to it
                if parent_team.current_size == course.team_size:
                    Memberrequest.objects.filter(team=parent_team,status="pending").update(status="rejected")

                context_dict['message'] = "%s has now been merged with %s" % (child_team.name, parent_team.name)
                context_dict['merge'] = True


    return render(request, 'teambuilder/merge_teams.html', context_dict)



