from django.conf.urls import patterns, url

urlpatterns = patterns('backend.blog.api_views',
    # Examples:
    url(r'^newest/$', 'newest', name='newest'),
    url(r'^posts/$', 'posts', name='blog_posts'),
    url(r'^posts/(?P<slug>[\w-]+)', 'specific_post'),
)
