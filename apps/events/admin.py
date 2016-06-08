from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Общая информация', {'fields': ['name', 'info', 'is_special', 'is_active']}),
        ('Информация об артистах', {'fields': ['artists', 'style']}),
        ('Информация о дате', {'fields': ['date', 'start']}),
        ('Информация о стоимости', {'fields': ['discounts', 'price']}),
        ('Афиша', {'fields': ['poster']}),
    ]

    def start_format(self, obj):
        return obj.start.strftime("%H:%M")
    start_format.admin_order_field = 'start'
    start_format.short_description = 'Начало'

    def date_format(self, obj):
        return obj.date.strftime("%d.%m.%Y")
    date_format.admin_order_field = 'date'
    date_format.short_description = 'Дата'

    list_display = ('name', 'is_special', 'artists', 'date_format', 'start_format', 'price')
    list_filter = ['is_special', 'date', 'price']
    #list_editable = ['is_special']
    search_fields = ['name']
    date_hierarchy = 'date'

admin.site.register(Event, EventAdmin)
