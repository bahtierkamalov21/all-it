from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'projects/images', views.ProjectImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
