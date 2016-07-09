from django import template

from ..models import RoomPackage

register = template.Library()


@register.inclusion_tag('partials/available_room_packages.html')
def available_room_packages(product, room):
    qs = RoomPackage.objects.filter(room_type=room.room_type)
    return {
        'room': room,
        'available': qs.count(),
        'packages_list': qs,
    }
