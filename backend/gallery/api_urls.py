"""
URL handlers for gallery API
"""

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'backend.gallery.api_views',
    url(r'^images/$', 'images', name='gallery_images'),
    #url(r'^images/(?P<slug>[\w-]+)', 'specific_image'),
)
