from datetime import datetime, date
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Skill(models.Model):
    skill_name=models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.skill_name

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    phone_number = models.CharField(max_length=15, null=True)
    dob=models.DateField(default=date.today(), null=True)
    about_me=models.TextField(max_length=500, null=True)


    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class UserProfile_Skill(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    skill = models.ForeignKey(Skill)


    def __unicode__(self):
        return self.user_profile + "_" + self.skill


class Course(models.Model):
    code=models.CharField(max_length=15,unique=True)
    name=models.CharField(max_length=100,unique=True)
    course_password=models.CharField(max_length=15)
    team_size=models.IntegerField(default=0)
    add_date=models.DateField(default=datetime.now(), null=False)
    creator=models.ForeignKey(User)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Team(models.Model):
    name=models.CharField(max_length=100, unique=True)
    course=models.ForeignKey(Course)
    creator = models.ForeignKey(User)
    current_size=models.IntegerField(default=0)
    creation_date=models.DateField(default=datetime.now(), null=False)
    required_skills=models.TextField(max_length=500)
    description=models.TextField(max_length=500)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    def __unicode__(self):
         return self.name

class Memberrequest(models.Model):
    user=models.ForeignKey(User)
    status=models.CharField(max_length=10, default="pending")
    request_date=models.DateField(default=datetime.now(), null=False)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return  self.user.username + "," + self.team