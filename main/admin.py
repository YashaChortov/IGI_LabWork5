
from .models import Manufacturer, ProductType, Product, Client, Employee, Order, FAQ, Contact

from django.contrib import admin

admin.site.register(FAQ)



@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'manufacturer', 'product_type', 'created_at')
    list_filter = ('manufacturer', 'product_type')
    search_fields = ['name']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'city', 'birth_date')
    search_fields = ['full_name', 'email', 'city']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'phone', 'email', 'birth_date')
    search_fields = ['full_name', 'position']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'product', 'quantity', 'order_date', 'delivery_date')
    list_filter = ('order_date', 'delivery_date')
    search_fields = ['client__full_name', 'product__name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'job_description', 'email', 'phone')
    search_fields = ['name']

