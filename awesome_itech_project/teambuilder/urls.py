from django.conf.urls import patterns, include, url
from teambuilder import views

app_name = 'teambuilder'
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^reset-passord/$', views.reset_password, name='reset'),
    url(r'^login/$', views.login, name='login'),
    url(r'^create-team/$', views.create_team, name='create_team'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^team/(?P<team_name_slug>[\w\-]+)/details/$', views.team_details, name='team_detail'),
    url(r'^find-team/$', views.find_team, name='find_team'),
)