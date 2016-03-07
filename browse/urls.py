from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /browse/
    url(r'^$', views.index, name='index'),

    # ex: /browse/year/2000/
    url(r'^year/(?P<year>[0-9]+)/$', views.year, name='year'),

    # ex: /browse/issue/6/
    url(r'^issue/(?P<issue_id>[0-9]+)/$', views.issue, name='issue'),

    # ex: /browse/article/5/
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article, name='article'),

]
