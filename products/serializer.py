from rest_framework import serializers

from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # 전부다 넣고싶을 때, 각각 넣으려면 [ ]