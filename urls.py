from django.conf.urls.defaults import *
from django.contrib import admin
from settings import MEDIA_ROOT, DJANGO_STATIC
import views
import models

admin.site.register(models.Case)
admin.site.register(models.Script)

urlpatterns = patterns('',
     (r'^/?$', views.index),
     (r'^cases/(?P<id>[0-9]+)$', views.case),
     (r'^cases/(?P<id>[0-9]+)/run$', views.runcase),
     (r'^admin/', include(admin.site.urls)),
)

if DJANGO_STATIC:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    )