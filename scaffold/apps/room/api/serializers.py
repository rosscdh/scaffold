from rest_framework import serializers

from oscar.apps.partner.models import Partner
from scaffold.apps.catalogue.api.serializers import ProductSerializer
from ..models import RoomPackage


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner


class RoomPackageSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()
    partner = PartnerSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = RoomPackage

    def get_amount(self, obj):
        return {
            'amount': obj.amount.amount,
            'currency': str(obj.amount.currency),
        }
