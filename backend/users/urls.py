from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'requests', views.RequestUserViewSet)
router.register(r'requests/images', views.RequestUserImageViewSet)
router.register(r'reviews', views.UserReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
