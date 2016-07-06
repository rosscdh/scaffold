# -*- coding: UTF-8 -*-
from scaffold.utils import get_namedtuple_choices
from django.utils.translation import ugettext_lazy as _


ROOM_TYPES = get_namedtuple_choices('ROOM_TYPES', (
    ('std_room', 'std_room', _('Standard Room')),
    ('bedroom', 'bedroom', _('Bedroom')),
    ('kitchen', 'kitchen', _('Kitchen')),
    ('toilet', 'toilet', _('Toilet')),
    ('bathroom', 'bathroom', _('Bathroom')),
    ('sauna', 'sauna', _('Sauna')),
    ('jacuzzi', 'jacuzzi', _('Jacuzzi')),
))


