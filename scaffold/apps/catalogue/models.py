# -*- coding: UTF-8 -*-
from django.db import models
from jsonfield import JSONField

from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    data = JSONField(default={})


#
# Must import oscar products here
#
from oscar.apps.catalogue.models import *