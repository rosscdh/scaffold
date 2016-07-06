# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import HomePageView

urlpatterns = patterns('',
                       url(r'^$',
                           HomePageView.as_view(),
                           name='index'),)
