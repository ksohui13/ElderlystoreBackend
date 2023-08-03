from typing import Any
from django.db import models
from order.models import order, order_detail
from django.db.models.query import QuerySet
from django.views import View
from django.views.generic import ListView
# Create your models here.

class OrderList(ListView):
    template_name = "order.html"
    context_object_name = 'order_list'

    