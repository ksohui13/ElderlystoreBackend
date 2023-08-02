from django.urls import path

from products.views import ProductView, ProductDetail

urlpatterns = [
    path('', ProductView.as_view()),
    path('/<int:product_id>', ProductDetail.as_view()),
]