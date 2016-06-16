from django.contrib import admin
from .models import House

#декоратор
@admin.register(House)
class AdminHouse(admin.ModelAdmin):
	list_display = ["name", "price", "id"]
