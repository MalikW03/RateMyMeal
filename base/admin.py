from django.contrib import admin

# Register your models here.

from .models import Review, User, FoodItem
admin.site.register(Review)
admin.site.register(User)
admin.site.register(FoodItem)