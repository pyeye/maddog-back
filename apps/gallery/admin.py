from django.contrib import admin

from .models import Image, Album


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


class AlbumAdmin(admin.ModelAdmin):

    def created_at_f(self, obj):
        return obj.created_at.strftime("%d.%m.%Y")
    created_at_f.admin_order_field = 'created_at'
    created_at_f.short_description = 'Созданно'

    inlines = [ImageInline]
    list_display = ('name', 'description', 'created_at_f')
    search_fields = ['name']
    date_hierarchy = 'created_at'


class ImageAdmin(admin.ModelAdmin):
    def created_at_f(self, obj):
        return obj.created_at.strftime("%d.%m.%Y")
    created_at_f.admin_order_field = 'created_at'
    created_at_f.short_description = 'Созданно'

    list_display = ('info', 'created_at_f')
    date_hierarchy = 'created_at'


admin.site.register(Album, AlbumAdmin)
admin.site.register(Image, ImageAdmin)
