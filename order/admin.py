from django.contrib import admin
from order.models import Order, OrderItem, OrderItemStatus, OrderStatus

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderItemStatus)
admin.site.register(OrderStatus)