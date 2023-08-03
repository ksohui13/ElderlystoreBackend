from django.db       import models
from mainshop.models     import TimeStampModel
from accounts.models    import User
from products.models import Product

class Order(TimeStampModel):
    order_number       = models.CharField(max_length=100)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

class OrderStatus(TimeStampModel):
    status = models.CharField(max_length=100)

    class Meta:
        db_table = 'order_status'

class OrderItem(TimeStampModel):
    quantity          = models.IntegerField(default=0)
    product           = models.ForeignKey(Product, on_delete=models.CASCADE)
    order             = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_item_status = models.ForeignKey('OrderItemStatus',on_delete=models.CASCADE)

    class Meta:
        db_table = 'order_items'

class OrderItemStatus(TimeStampModel):
    status = models.CharField(max_length=100)

    class Meta:
        db_table = 'order_item_status'

class Shipping(TimeStampModel):
    tracking_number = models.CharField(max_length=100)          #송장번호
    date            = models.DateField()                        #배송 날짜
    message         = models.CharField(max_length=100)          #배송메세지
    detail          = models.CharField(max_length=200)          #상세메세지
    order           = models.ForeignKey('Order', on_delete=models.CASCADE)  #주문내역
    order_item      = models.ManyToManyField('OrderItem', through='ShippingItem')   #주문상품

    class Meta:
        db_table = 'shipping'

class ShippingItem(TimeStampModel):
    shipping   = models.ForeignKey('Shipping', on_delete=models.CASCADE)    #배송
    order_item = models.ForeignKey('OrderItem', on_delete=models.CASCADE)   #주문 상품

    class Meta:
        db_table = 'shipping_order_items'