from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','productName','unitPrice','quantity', 'date_created','date_modified')
        read_only_fields = ('date_created','date_modified')
