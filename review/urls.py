from django.urls import include, path
from rest_framework.routers import DefaultRouter
import review.views

router = DefaultRouter()
router.register('review', review.views.ReviewViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('review/', review.views.ReviewList.as_view()),
    path('review/<int:pk>',review.views.ReviewDetail.as_view())
]