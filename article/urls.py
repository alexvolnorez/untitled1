__author__ = 'admin'
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^1/', 'article.views.basic_one'),
    url(r'^2/', 'article.views.temlate_two'),
    url(r'^3/', 'article.views.temlate_three_simple'),
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
    url(r'^$', 'article.views.articles'),
]
