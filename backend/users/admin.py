from django.contrib import admin
from .models import CustomUser, RequestUser, RequestUserImage, UserReview, PopularReview

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(RequestUser)
admin.site.register(RequestUserImage)
admin.site.register(UserReview)
admin.site.register(PopularReview)
