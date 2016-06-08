from django.contrib import admin

from .models import Menu, Price


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    inlines = [PriceInline]


admin.site.register(Menu, MenuAdmin)
