from typing import Any
from django.db import models
from order.models import order, order_detail
from django.db.models.query import QuerySet
from django.http import HttpResponseForbidden
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
# Create your models here.

@login_required
class OrderList(ListView):
    template_name = "order.html"
    context_object_name = 'order_list'

    #로그인된 사용자의 정보와 일치하는 주문서 가져와서 queryset에 저장하기
    