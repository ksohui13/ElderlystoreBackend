from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

@login_required
class OrderList(ListView):
    template_name = "order.html"
    context_object_name = 'order_list'

    #로그인된 사용자의 정보와 일치하는 주문서 가져와서 queryset에 저장하기
    