from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'requests', views.RequestUserViewSet)
router.register(r'requests-images', views.RequestUserImageViewSet)
router.register(r'users_reviews', views.UserReviewViewSet)
router.register(r'populars_reviews', views.PopularReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reset_password/', views.reset_password_and_email_send_code),
    path('decoded_tokens/', views.decoded_tokens)
]
