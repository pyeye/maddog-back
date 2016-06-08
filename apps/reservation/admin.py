from django.contrib import admin

from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):

    def time_format(self, obj):
        return obj.start.strftime("%H:%M")
    start_format.admin_order_field = 'time'
    start_format.short_description = 'Время'

    def date_format(self, obj):
        return obj.date.strftime("%d.%m.%Y")
    date_format.admin_order_field = 'date'
    date_format.short_description = 'Дата'

    list_display = ('phone_number', 'name', 'date_format', 'time_format', 'count_people', 'is_vip', 'status')
    list_filter = ['is_vip', 'status']
    list_editable = ['status']
    search_fields = ['phone_number']

admin.site.register(Reservation, ReservationAdmin)
