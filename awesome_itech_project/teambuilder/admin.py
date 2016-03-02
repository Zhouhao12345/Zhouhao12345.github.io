from django.contrib import admin
from teambuilder.models import Team, UserProfile, User, Course, Memberrequest, Skill


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'dob', 'about_me', 'user')


# Register your models here.
admin.site.register(Team)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Course)
admin.site.register(Memberrequest)
admin.site.register(Skill)
