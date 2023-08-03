from django.urls import path, include
from .views import Order, OrderItem, Shipping
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
