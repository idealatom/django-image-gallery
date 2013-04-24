from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from example.app.views import *

urlpatterns = patterns('',
    url(r'^$', GalleryList.as_view()),
    url(r'^add/$', AddGallery.as_view(), name='add'),

    url(r'^image_gallery/', include('image_gallery.urls', namespace='image_gallery')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
   )
