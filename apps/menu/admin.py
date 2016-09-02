from django.contrib import admin

from .models import Menu, Price, Category, Group, Set, MenuSet


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    inlines = [PriceInline]

    def created_at_f(self, obj):
        return obj.created_at.strftime("%d.%m.%Y")
    created_at_f.admin_order_field = 'created_at'
    created_at_f.short_description = 'Созданно'

    def prices(self, obj):
        return obj.prices.all()

    list_display = ('name', 'description', 'created_at_f', 'is_active', 'prices')
    list_filter = ['is_active']
    #list_editable = ['is_special']
    search_fields = ['name']
    date_hierarchy = 'created_at'


class MenuSetInline(admin.TabularInline):
    model = MenuSet
    extra = 2


class SetAdmin(admin.ModelAdmin):
    inlines = [MenuSetInline, PriceInline]

    def created_at_f(self, obj):
        return obj.created_at.strftime("%d.%m.%Y")
    created_at_f.admin_order_field = 'created_at'
    created_at_f.short_description = 'Созданно'

    def prices(self, obj):
        return obj.prices.all()

    list_display = ('name', 'description', 'created_at_f', 'is_active', 'prices')
    list_filter = ['is_active']
    #list_editable = ['is_special']
    search_fields = ['name']
    date_hierarchy = 'created_at'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    search_fields = ['name']


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ['name']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Set, SetAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Group, GroupAdmin)

