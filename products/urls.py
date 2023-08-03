from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import products.views
from products.views import ProductView, ProductDetailView

#참고 https://velog.io/@dustndus8/DjangoDRF-%EC%83%81%ED%92%88-%EB%A6%AC%EB%B7%B0-API-%EB%A7%8C%EB%93%A4%EA%B8%B0

router = DefaultRouter()
router.register('product', products.views.ProductViewSet) # viewset이 만든 여러 메소드의 url을 만들어줌
urlpatterns = [
    path('', include(router.urls)),
    path('', ProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
]