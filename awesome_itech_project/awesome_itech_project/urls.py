from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

class MyRegistrationView(RegistrationView):
    form_class=RegistrationFormUniqueEmail
    def get_success_url(self, user):
        return '/teambuilder/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'awesome_itech_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^teambuilder/', include('teambuilder.urls', namespace='teambuilder')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
