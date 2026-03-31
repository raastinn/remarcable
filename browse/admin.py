from django.contrib import admin
from .models import Category, Tag, Product


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "category", "price", "created_at")
    list_filter = ("category", "tags")
    search_fields = ("comment", "description")
    filter_horizontal = ("tags",)
