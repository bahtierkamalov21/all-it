from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'projects_images', views.ProjectImageViewSet)
router.register(r'stacks', views.StackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user_projects/', views.getProjectsUser),
    path('project_slug/', views.getProjectSlug),
]
