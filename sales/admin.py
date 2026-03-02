from django.contrib import admin
from .models import Sale, SaleItem


class SaleItemInline(admin.TabularInline):

    model = SaleItem

    extra = 0


class SaleAdmin(admin.ModelAdmin):

    inlines = [SaleItemInline]

    list_display = ('id','user','total','created')


admin.site.register(Sale, SaleAdmin)