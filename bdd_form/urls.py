from django.conf.urls import url

from . import views # import views so we can use them in urls.
from django.views.static import serve 

urlpatterns = [
    url(r'^$', views.dashboard), 
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

