from django.contrib import admin
from django.utils.html import format_html
from .models import Photo
import os

# PhotoAdmin class defined, inherits from admin.ModelAdmin
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag')
    search_fields = ('title',)
    readonly_fields = ('image_preview',)

    def image_tag(self, obj):
        return format_html('<img src="/static/imgs/{}" width="50" height="50" />'.format(os.path.basename(obj.image.name)))
    image_tag.short_description = 'Image'

    def image_preview(self, obj):
        return format_html('<img src="/static/imgs/{}" width="200" height="200" />'.format(os.path.basename(obj.image.name)))
    image_preview.short_description = 'Current Image'

admin.site.register(Photo, PhotoAdmin)
