"""
URL handlers for authentication API
"""

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'backend.authentication.api_views',
    url(r'^login/', 'login'),
    url(r'^logout/', 'logout'),
    url(r'^verify/', 'verify'),
)
