from django.conf.urls import patterns, url

urlpatterns = patterns('backend.auth.api_views',
    # Examples:
    url(r'^login/', 'login'),
    url(r'^logout/', 'logout'),
    url(r'^verify/', 'verify'),
)
