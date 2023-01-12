from django.urls import path
from . import views

urlpatterns = [
    path('reset_password/', views.reset_password_and_email_send_code),
]
