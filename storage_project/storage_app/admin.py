from django.contrib import admin
from .models import Category, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en', 'category_code')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'category', 'code', 'internal_code', 'package_length', 'package_width', 'package_height', 'name_ru',
        'description_ru', 'description_en', 'amount', 'cost', 'is_active')
