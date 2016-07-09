from rest_framework import serializers

from oscar.apps.promotions.models import Image
from oscar.apps.catalogue.models import ProductImage

from ..models import Product


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
