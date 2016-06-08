from django.contrib import admin

from .models import Menu, Price


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    inlines = [PriceInline]

    def created_at_f(self, obj):
        return obj.date.strftime("%d.%m.%Y")
    created_at_f.admin_order_field = 'created_at'
    created_at_f.short_description = 'Созданно'

    def prices(self, obj):
        return obj.prices.all()
    created_at_f.short_description = 'Цены'

    list_display = ('name', 'description', 'created_at_f', 'is_lunch', 'is_active', 'prices')
    list_filter = ['is_active', 'is_lunch']
    #list_editable = ['is_special']
    search_fields = ['name']
    date_hierarchy = 'created_at'


admin.site.register(Menu, MenuAdmin)
