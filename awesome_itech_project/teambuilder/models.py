from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    phonenumber = models.CharField(max_length=15)
    dob=models.DateField(default=datetime.now())
    aboutme=models.TextField(max_length=500)


    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.id

class Memberrequest(models.Model):
    user=models.ForeignKey(User)
    status=models.CharField(max_length=10)
    request_date=models.DateField(default=datetime.now())

    def __unicode__(self):
        return  self.status

class Skill(models.Model):
    user=models.ForeignKey(User)
    skill_name=models.CharField(max_length=20)

    def __unicode__(self):
        return  self.skill_name

class Course(models.Model):
    code=models.CharField(max_length=15,unique=True)
    name=models.CharField(max_length=100,unique=True)
    course_password=models.CharField(max_length=15)
    team_size=models.IntegerField(default=0)
    add_date=models.DateField(default=datetime.now())
    creator=models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Role(models.Model):
    type=models.CharField(max_length=15,unique=True)
    role_id=models.IntegerField(default=0,unique=True)

    def __unicode__(self):
        return  self.type

class UserRole(models.Model):
    user=models.ForeignKey(User)
    role=models.ForeignKey(Role)

class Team(models.Model):
    name=models.CharField(max_length=100, unique=True)
    course=models.ForeignKey(Course)
    current_size=models.IntegerField(default=0)
    creation_date=models.DateField(default=datetime.now())
    required_skills=models.TextField(max_length=500)
    description=models.TextField(max_length=500)

    def __unicode__(self):
         return self.name