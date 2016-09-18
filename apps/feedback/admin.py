from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):

    def date_format(self, obj):
        return obj.created_at.strftime("%d.%m.%Y")
    date_format.admin_order_field = 'date'
    date_format.short_description = 'Дата'

    list_display = ('contact', 'created_at')
    list_filter = ['created_at']
    search_fields = ['contact']

admin.site.register(Feedback, FeedbackAdmin)
