from django.contrib import admin

# Register your models here.

from .models import Review, User
admin.site.register(Review)
admin.site.register(User)
