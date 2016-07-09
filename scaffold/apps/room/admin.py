from django.contrib import admin

from .models import Room, RoomPackage

admin.site.register([Room, RoomPackage])
