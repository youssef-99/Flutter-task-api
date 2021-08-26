from rest_framework import serializers, fields
from rest_framework.utils.serializer_helpers import ReturnDict

from product.models import *


class CustomMultipleChoiceField(fields.MultipleChoiceField):
    def to_representation(self, value):
        print(value)
        return super().to_representation(value)


class ProductSerializer(serializers.ModelSerializer):
    client_type = fields.MultipleChoiceField(choices=Product.TYPE_CHOICES)
    available_sizes = fields.MultipleChoiceField(choices=Product.SIZE_CHOICES)

    class Meta:
        model = Product
        fields = ['title', 'description', 'available_sizes', 'price',
                  'picture', 'client_type', 'product_specification', 'rate']


class SpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecifications
        fields = ['id', 'type', 'category']


