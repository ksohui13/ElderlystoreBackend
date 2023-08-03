from django.db import models

#수정해야함
class OrderStatus(models.Model):
    order_status = models.CharField(max_length=100)         #주문 상태
