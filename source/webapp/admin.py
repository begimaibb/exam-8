from django.contrib import admin

# Register your models here.
from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'picture']
    list_display_links = ['name']
    list_filter = ['name', 'category']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'category', 'picture']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
