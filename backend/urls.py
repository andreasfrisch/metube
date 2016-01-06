"""
Author: Andreas Frisch
"""

from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns(
#     '', #no default namespace for root urls.py
#     url(r'^$', 'backend.views.home', name='metube_home'),
#     url(r'^api/', include([
#         url(r'^auth/', include('backend.authentication.api_urls')),
#         url(r'^blog/', include('backend.blog.api_urls')),
#         url(r'^gallery/', include('backend.gallery.api_urls')),
#
#     ])),
#     url(r'^admin/', include(admin.site.urls)),
# )

#TODO:
#for development only
#shouldn't host media files like this. Instead it needs separate server
urlpatterns = [
    url(r'^$', 'backend.views.home', name='metube_home'),
    url(r'^api/', include([
        url(r'^auth/', include('backend.authentication.api_urls')),
        url(r'^blog/', include('backend.blog.api_urls')),
        url(r'^gallery/', include('backend.gallery.api_urls')),

    ])),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
