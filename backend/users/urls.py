from django.urls import path, include
from rest_framework import routers
from . import views
from . import authentication

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'users_reviews', views.UserReviewViewSet)
router.register(r'populars_reviews', views.PopularReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('username_phone_number/', authentication.getUsernameOnPhoneNumber),
    path('decoded_tokens/', views.decoded_tokens)
]
