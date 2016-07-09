# -*- coding: UTF-8 -*-
from django.conf.urls import url

from scaffold.apps.room.api.views import RoomPackagesApiView, RoomPackageDetailApiView


urlpatterns = [
    url(r'^rooms/(?P<room_pk>[\d]+)/packages/$',
        RoomPackagesApiView.as_view(), name='room_packages'),
    url(r'^rooms/(?P<room_pk>[\d]+)/packages/(?P<pk>[\d]+)/$',
        RoomPackageDetailApiView.as_view(), name='room_package_detail'),
]
