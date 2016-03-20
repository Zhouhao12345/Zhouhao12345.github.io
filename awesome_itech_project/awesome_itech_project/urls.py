from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail
from django.conf import settings

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

# let's just use django for now to serve static media as our application does not anticipate any load at the moment
urlpatterns += patterns(
    'django.views.static',
    (r'^media/(?P<path>.*)',
    'serve',
    {'document_root': settings.MEDIA_ROOT}), )
