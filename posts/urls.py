from django.conf.urls import patterns, url
from posts import views

urlpatterns = patterns("",
   url(r'^$', views.PostList.as_view()),
   url(r'^users/$', views.UserList.as_view()),
   url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
   url(r'^test/$', views.TestModelList.as_view()),
   url(r'^(?P<pk>\d+)/$', views.PostDetail.as_view()),
)