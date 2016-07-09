# -*- coding: UTF-8 -*-
from django.db import models

from jsonfield import JSONField
from djmoney.models.fields import MoneyField
from versatileimagefield.fields import VersatileImageField

from . import ROOM_TYPES


class Room(models.Model):
    ROOM_TYPE_CHOICES = ROOM_TYPES

    feature_image = VersatileImageField(
        'Image',
        upload_to='images/rooms/',
        null=True,
        blank=True
    )
    product = models.ForeignKey('catalogue.Product')

    room_type = models.CharField(max_length=64,
                                 choices=ROOM_TYPE_CHOICES.get_choices(),
                                 default=ROOM_TYPE_CHOICES.std_room)

    name = models.CharField(max_length=255)
    short_description = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)

    data = JSONField(default={})

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.ROOM_TYPE_CHOICES.get_desc_by_value(self.room_type))

    @property
    def display_type(self):
        return self.ROOM_TYPE_CHOICES.get_desc_by_value(self.room_type)


class RoomPackage(models.Model):
    ROOM_TYPE_CHOICES = ROOM_TYPES

    room_type = models.CharField(max_length=64,
                                 choices=ROOM_TYPE_CHOICES.get_choices(),
                                 default=ROOM_TYPE_CHOICES.std_room)

    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    partner = models.ForeignKey('partner.Partner', blank=True, null=True)
    products = models.ManyToManyField('catalogue.Product', blank=True)
    short_description = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return '%s (%s)' % (self.amount, self.ROOM_TYPE_CHOICES.get_desc_by_value(self.room_type))
