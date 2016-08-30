from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ['user', ]

admin.site.register(UserProfile)
