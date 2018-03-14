from django.contrib import admin
from .models import *
# Register your models here.


class PhotoInline(admin.TabularInline):
    readonly_fields = ['image_img', ]
    list_display = ['image_img']
    model = Photo
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    inlines = [PhotoInline]




