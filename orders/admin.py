from django.contrib import admin
from .models import Order, ConatacForm


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["product", "name", "phone", "date"]


@admin.register(ConatacForm)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["name", "telephone", "date"]