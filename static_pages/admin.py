from django.contrib import admin
from .models import Page, Work
# Register your models here


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Work)