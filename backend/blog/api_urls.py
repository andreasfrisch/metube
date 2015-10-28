"""
URL handlers for blog API
"""

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'backend.blog.api_views',
    url(r'^newest/$', 'newest', name='newest'),
    url(r'^posts/$', 'posts', name='blog_posts'),
    url(r'^posts/(?P<slug>[\w-]+)', 'specific_post'),
)
