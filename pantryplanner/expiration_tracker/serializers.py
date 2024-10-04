from rest_framework import serializers
from .models import PantryItem


class PantryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantryItem
        fields = (
            "id",
            "item_type",
            "brand",
            "quantity",
            "unit",
            "purchase_date",
            "expiration_date",
        )
