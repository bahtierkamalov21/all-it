from django.contrib import admin
from .models import CustomUser, UserReview, PopularReview

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserReview)
admin.site.register(PopularReview)
