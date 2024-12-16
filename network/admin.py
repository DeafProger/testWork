from network.models import Supplier, Contact, Product
from django.contrib import admin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'city',)
    list_display_links = ['id', 'country']
    list_filter = ('country', 'city',)


@admin.action(description='Clear debt')
def set_null_debts(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'company_name', 'supplier_name', 'debt',
        'level', 'contacts',
    )
    list_filter = ('contacts__city', 'contacts__country',)
    list_display_links = ['id', 'supplier_name']
    search_fields = ('id', 'company_name', 'level',)
    actions = [set_null_debts]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'supplier')
    list_filter = ('supplier__contacts__city', 'supplier__contacts__country',)
    list_display_links = ['title']
