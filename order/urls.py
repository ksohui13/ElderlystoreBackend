from django.urls import path, include
from .views import Order, OrderItem, Shipping
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router url 연결 어디로 할건지 적어줘야해!
#ex) router.register('list', QuestViewSet) >> 나중에 localhost:8000/api/order/list로 연결됨

# urlpatterns =[
#     path('', include(router.urls)),
# ]
