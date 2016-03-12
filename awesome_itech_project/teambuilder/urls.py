from django.conf.urls import patterns, include, url
from teambuilder import views

app_name = 'teambuilder'
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^reset-password/$', views.reset_password, name='reset'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^create-team/$', views.create_team, name='create_team'),
    url(r'^add-course/$', views.add_course, name='add_course'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^team/(?P<team_name_slug>[\w\-]+)/details/$', views.team_details, name='team_detail'),
    url(r'^find-team/$', views.find_team, name='find_team'),
    url(r'^team/(?P<team_name_slug>[\w\-]+)/send-request/$', views.join_team, name='join_team'),
    url(r'^team/(?P<team_name_slug>[\w\-]+)/cancel-request/$', views.cancel_request, name='cancel_request'),
    url(r'^team/(?P<team_name_slug>[\w\-]+)/view-requests/$', views.view_requests, name='view_requests'),
    url(r'^request/(?P<request_id>[\w\-]+)/accept/$', views.accept_request, name='accept_request'),
    url(r'^request/(?P<request_id>[\w\-]+)/reject/$', views.reject_request, name='reject_request'),
)