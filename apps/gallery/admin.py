from django.contrib import admin

from .models import Image, Album


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Image)
