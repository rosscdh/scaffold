from django import forms
from django.forms.models import inlineformset_factory

from scaffold.apps.catalogue.models import Product
from scaffold.apps.room.models import Room


class ProductRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'product',
            'room_type',
            'name',
            'feature_image',
            'short_description',
            'description',
        ]


BaseProductRoomFormSet = inlineformset_factory(
    Product, Room, form=ProductRoomForm, extra=2)


class ProductRoomFormSet(BaseProductRoomFormSet):

    def __init__(self, product_class, user, *args, **kwargs):
        super(ProductRoomFormSet, self).__init__(*args, **kwargs)
