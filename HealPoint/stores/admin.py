from django.contrib import admin
from .models import Store

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "city", "created_at")
    list_filter = ("is_active", "state")
    search_fields = ("name",)
    list_per_page = 10
