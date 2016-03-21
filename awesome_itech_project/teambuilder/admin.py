from django.contrib import admin
from teambuilder.models import Team, UserProfile, Course, Memberrequest


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'about_me', 'user')

class MemberRequestAdmin(admin.ModelAdmin):
    list_display = ('user' , 'team', 'status', )

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'course')


# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Course)
admin.site.register(Memberrequest, MemberRequestAdmin)
