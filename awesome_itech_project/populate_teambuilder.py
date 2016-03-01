import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'awesome_itech_project.settings')

import django
django.setup()

from teambuilder.models import Team, UserProfile, UserRole, Course, Memberrequest, Skill, Role
from django.contrib.auth.models import User

def populate():
    user = add_user("user1", "abcdef", "abc@xyz.com")
    user2 = add_user("user2", "abcdef", "def@xyz.com")
    user3 = add_user("user3", "abcdef", "ghi@xyz.com")
    user4 = add_user("user4", "abcdef", "jkl@xyz.com")
    user5 = add_user("user5", "abcdef", "mno@xyz.com")
    user6 = add_user("user6", "abcdef", "pqr@xyz.com")
    add_userprofile("01234567890", "just a regular guy", user)
    add_userprofile("01238747890", "just another regular guy", user2)
    add_userprofile("01299854740", "just another regular guy again", user3)
    add_userprofile("01255555590", "just another regular guy", user4)
    add_userprofile("07778585840", "just another regular guy again", user5)
    add_userprofile("00125698580", "just another regular guy", user6)

    course = add_course("COMP0123","Internet Technology", "ITECH2016", 4, user2)
    course2 = add_course("COMP0144","Advanced programming", "AP2016", 5, user2)
    team = add_team("Awesome",course, user,"Java, CSS", "Team for ITECH project")
    team2 = add_team("Bandbud",course2, user2,"Java, CSS", "Team for AP project")
    team3 = add_team("Excurj",course, user3,"Java, CSS", "Team for ITECH project")
    team4 = add_team("Nameless",course2, user4,"Java, CSS", "Team for AP project")
    team5 = add_team("Crazy",course, user6,"Java, CSS", "Team for ITECH project")
    team6 = add_team("Happy",course2, user5,"Java, CSS", "Team for AP project")
    add_member_request(user2,team)
    add_member_request(user3,team5)
    add_member_request(user4,team2)
    add_member_request(user5,team4)
    add_member_request(user6,team3)
    add_member_request(user,team6)
    role1 = add_role("Student")
    role2 = add_role("Coordinator")
    assign_role(user,role1)
    assign_role(user2,role2)
    assign_role(user3,role1)
    assign_role(user4,role1)
    assign_role(user5,role2)
    assign_role(user6,role1)
    add_skill(user,"python programming")
    add_skill(user2,"Java programming")
    add_skill(user3,"C++")
    add_skill(user4,"perl")
    add_skill(user5,"Javascript")
    add_skill(user6,"Ruby on rails")

def add_user(username, password, email):
    user = User.objects.get_or_create(username=username)[0]
    user.set_password(password)
    user.email = email
    user.save()
    return user

def add_userprofile(phone, aboutme, user):
    u = UserProfile.objects.get_or_create(user=user)[0]
    u.phone_number = phone
    u.about_me = aboutme
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

def add_role(role):
    r = Role.objects.get_or_create(type=role)[0]
    return r

def assign_role(user, role):
    r = UserRole.objects.get_or_create(user=user, role = role)[0]
    return r

def add_skill(user, skill):
    s = Skill.objects.get_or_create(user=user, skill_name=skill)
    return s;

def add_member_request(user,team):
    a = Memberrequest.objects.get_or_create(user=user,team=team)
    return a



if __name__ == '__main__':
    print "Starting teambuilder population script..."
    populate()