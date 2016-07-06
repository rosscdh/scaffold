# -*- coding: UTF-8 -*-
from django.db import models
from jsonfield import JSONField

from . import ROOM_TYPES


class Room(models.Model):
    ROOM_TYPE_CHOICES = ROOM_TYPES

    product = models.ForeignKey('catalogue.Product')

    room_type = models.CharField(max_length=64,
                                 choices=ROOM_TYPE_CHOICES.get_choices(),
                                 default=ROOM_TYPE_CHOICES.std_room)

    name = models.CharField(max_length=255)
    short_description = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)

    data = JSONField(default={})
