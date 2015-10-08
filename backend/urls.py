from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'backend.views.home', name='metube_home'),
    url(r'^api/', include([
        url(r'^blog/', include('backend.blog.api_urls')),
        url(r'^auth/', include('backend.auth.api_urls'))
    ])),
    
    url(r'^admin/', include(admin.site.urls)),
)
