from django.conf.urls import patterns, url

urlpatterns = patterns('backend.blog.api_views',
    # Examples:
    url(r'^posts/(?P<slug>[\w-]+)', 'specific_post'),
    url(r'^posts/', 'posts', name='blog_posts'),
)
