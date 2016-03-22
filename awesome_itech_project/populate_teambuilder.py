import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'awesome_itech_project.settings')

import django
django.setup()

from teambuilder.models import Team, UserProfile, Course, Memberrequest
from django.contrib.auth.models import User

def populate():

    user = add_user("leifos", "leifos", "leifos@gmail.com")
    user2 = add_user("laura", "laura", "laura@gmail.com")
    user3 = add_user("david", "david", "david@gmail.com")
    user4 = add_user("yu", "yu", "yu@gmail.com")
    user5 = add_user("hao", "hao", "hao@gmail.com")
    user6 = add_user("gozie", "gozie", "gozie@gmail.com")
    user7 = add_user("jeff", "jeff", "jeff@gmail.com")


    userprofile1 = add_userprofile("01234567890", "I am the lecturer of Internet technology", user, 'coordinator')
    userprofile2 = add_userprofile("01238747890", "I am an industrial visitor", user2, 'student')
    userprofile3 = add_userprofile("01299854740", "I am an industrial visitor too", user3, 'student')
    userprofile4 = add_userprofile("01255555590", "I am a hardworking IT student", user4, 'student')
    userprofile5 = add_userprofile("07778585840", "I am a smart SD student", user5, 'student')
    userprofile6 = add_userprofile("00125698580", "I am a SD student, good at web development ", user6, 'student')
    userprofile7 = add_userprofile("00141698580", "I am a great SE student", user7, 'student')


    course = add_course("COMP0123","Internet Technology", "ITECH2016", 4, user)
    course2 = add_course("COMP0456","Programming", "PG2016", 4, user)

    team = add_team("Awesome",course, user6,"Java, CSS", "Team for ITECH project")
    team = add_team("Better",course2, user2,"Java, python", "Team for Programming project")
    team = add_team("Great",course2, user3,"Java, python", "Team for Programming project")


    add_member_request(user3,team)
    add_member_request(user4,team)
    add_member_request(user5,team)
    add_member_request(user6,team)
    add_member_request(user7,team)

    print "Database has been successfully populated!!!!!!!!!"

def add_user(username, password, email):
    user = User.objects.get_or_create(username=username)[0]
    user.set_password(password)
    user.email = email
    user.save()
    return user

def add_userprofile(phone, aboutme, user, role):
    u = UserProfile.objects.get_or_create(user=user)[0]
    u.phone_number = phone
    u.about_me = aboutme
    u.role = role
    u.save()
    return u

def add_course(code, name, cpassword, team_size, creator):
    c = Course.objects.get_or_create(code=code,name=name,course_password=cpassword,team_size=team_size,creator=creator)[0]
    return c

def add_team(name, course, creator, required_skills, description):
    t = Team.objects.get_or_create(name=name,course=course,creator=creator)[0]
    t.required_skills = required_skills
    t.description = description
    return t

def add_member_request(user,team):
    a = Memberrequest.objects.get_or_create(user=user,team=team)[0]
    return a

if __name__ == '__main__':
    print "Starting teambuilder population script..."
    populate()
