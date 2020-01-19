from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    url(r'^(?P<fid>\d+)/(?P<cid>\d+)/',views.getContent,name='content'),
    #url(r'^(?P<fid>\d+)/',views.getChapter,name='chapter'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
]
