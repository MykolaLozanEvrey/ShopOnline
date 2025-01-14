from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'price')
    list_display_links = ('name', 'price')
    search_fields = ('name', 'price',)
    prepopulated_fields = {'slug': ('name',)}
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
    
    
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


