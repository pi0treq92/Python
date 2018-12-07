from django.conf.urls import url
from django.urls import re_path
from blog import views

urlpatterns = [

    #utworzenie widoku dla strony poczatkowej
    url(r'^$', views.PostList.as_view(), name='post_list'),
    #utworzenie widoku dla strony o nas
    url(r'^about/$', views.About.as_view(), name='about'),
    #? question mark
    #d matches [0-9] and other digit characters.
    #'+' signifies that there must be at least 1 or more digits in the number
    url(r'^post/(?P<pk>\d+)$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^post/new/$', views.UtworzPost.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.UpdatePost.as_view(), name='post_update'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.UsuwaniePostu.as_view(), name='post_remove'),
    url(r'^drafts/$', views.DraftlistView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.dodawanie_komentarzy, name='dodawanie_komentarzy'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.zatwierdzanie_komentarzy, name='zatwierdzanie_komentarzy'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.usuwanie_komentarzy, name='usuwanie_komentarzy'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),


]
