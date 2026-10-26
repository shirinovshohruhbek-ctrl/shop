from django.contrib import admin
from import_export import admin as ie_admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Client, Product, Check
@admin.action()
def pruduct_soni(modeladmin, request, queryset):
    queryset.update(quantity=0)
@admin.action(description="ismini qosim qilish")
def client_ism(modeladmin, request, queryset):
    queryset.update(first_name="Qosimjon")
    queryset.update(username="00000000")
    queryset.update(email="")

@admin.register(Client)
class ClientAdmin(ie_admin.ImportExportActionModelAdmin):
    list_display = ('username', 'first_name')
    actions = ['pruduct_soni', 'client_ism']

@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    list_display = ('quality', 'name', 'price')
    actions = ['pruduct_soni', 'client_ism']

@admin.register(Check)
class CheckAdmin(ImportExportActionModelAdmin):
    list_display = ('client', 'product')

