from django.urls import include, path, re_path

from . import views


app_name = 'blog'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
