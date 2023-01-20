from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'users_reviews', views.UserReviewViewSet)
router.register(r'populars_reviews', views.PopularReviewViewSet)
router.register(r'category_notes', views.CategoryNoteViewSet)
router.register(r'notes', views.NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('decoded_tokens/', views.decoded_tokens)
]
