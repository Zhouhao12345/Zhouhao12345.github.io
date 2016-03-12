from django.contrib import admin
from teambuilder.models import Team, UserProfile, User, Course, Memberrequest, Skill


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'dob', 'about_me', 'user')

class MemberRequestAdmin(admin.ModelAdmin):
    list_display = ('user' , 'team', 'status')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator')


# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Course)
admin.site.register(Memberrequest, MemberRequestAdmin)
admin.site.register(Skill)
