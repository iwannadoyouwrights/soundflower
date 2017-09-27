from django.conf.urls import url
from main.views import *
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^id(?P<petal_id>\d{1,5})/$', views.petal, name="petal_info"),
    url(r'^mp(?P<project_id>\d{1,5})/$',
        MusicianProjectView.as_view(), name='project'),
    url(r'^mp(?P<project_id>\d{1,5})/album(?P<album_id>\d{1,5})/$',
        Album.as_view(), name='album'),
]
