# -*- coding: utf-8 -*-
from django.conf import settings


def scaffold_globals(request):
    return {
        'BASE_URL': getattr(settings, 'BASE_URL', None),
    }
