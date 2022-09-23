from decimal import Decimal
from rest_framework import serializers
from store.models import Collection, Product


class CollectionSerializer(serializers.Serializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            return serializers.ValidationError('Passwords don\'t match')
        return data
