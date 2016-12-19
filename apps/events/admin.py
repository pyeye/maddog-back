from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget

from .models import Event, Artist


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Общая информация', {'fields': ['name', 'info', 'is_special', 'is_active']}),
        ('Информация об артистах', {'fields': ['artists']}),
        ('Информация о дате', {'fields': ['date', 'start']}),
        ('Информация о стоимости', {'fields': ['discounts', 'price']}),
        ('Афиша', {'fields': ['poster']}),
        ('Дополнительно', {'fields': ['extra']}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    def start_format(self, obj):
        return obj.start.strftime("%H:%M")
    start_format.admin_order_field = 'start'
    start_format.short_description = 'Начало'

    def date_format(self, obj):
        return obj.date.strftime("%d.%m.%Y")
    date_format.admin_order_field = 'date'
    date_format.short_description = 'Дата'

    list_display = ('name', 'is_special', 'date_format', 'start_format', 'price')
    list_filter = ['is_special', 'date', 'price']
    filter_horizontal = ('artists',)
    #list_editable = ['is_special']
    search_fields = ['name']
    date_hierarchy = 'date'


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'style')
    list_filter = ['style']
    #list_editable = ['is_special']
    search_fields = ['name']

admin.site.register(Event, EventAdmin)
admin.site.register(Artist, ArtistAdmin)
