from rest_framework import serializers
from order.models import Order, OrderItem


class OrderSerializer(serializers.Serializer):
    order_number = serializers.ReadOnlyField(
        source = 'order.order_number'
    )

    class Meta:
        model = Order
        read_only_fields = '__all__'

class OrderItemSerializer(serializers.Serializer):
    class Meta:
        model: OrderItem
        read_only_fields = '__all__'