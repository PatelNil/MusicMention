from django.urls import path
from . import views
from django.conf.urls import url
app_name='music'
urlpatterns = [
    #path('',views.index,name='index'),
    url(r'^$',views.IndexView.as_view() ,name='index'),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='details'),
    url(r'album/add/$',views.Album_create.as_view(),name='album_add'),
    url(r'album/add_song/$',views.Song_add.as_view(),name='add_song'),
    url(r'album/(?P<pk>[0-9]+)/$',views.Album_update.as_view(),name='album_update'),
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.Album_delete.as_view(),name='album_delete'),
    url(r'album/(?P<pk>[0-9]+)/delete_song',views.Song_delete.as_view(),name='song_delete'),
    #url(r'^(?P<album_id>[0-9]+)/fav/$',views.fav,name='fav'),
]

 