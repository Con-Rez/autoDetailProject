from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from .models import Photo
from .models import Service
import os

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'time_to_complete', 'description')
    search_fields = ('name', 'description')
    list_filter = ('cost', 'time_to_complete')

# PhotoAdmin class defined, inherits from admin.ModelAdmin
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag')
    search_fields = ('title',)
    readonly_fields = ('image_preview',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Photo Gallery Administration'
        extra_context['subtitle'] = 'Manage your photo gallery with ease. Please upload photos with the same size for best results.'
        return super(PhotoAdmin, self).changelist_view(request, extra_context=extra_context)

    def image_tag(self, obj):
        return format_html('<img src="/static/imgs/{}" style="max-height:50px; width:auto;" />'.format(os.path.basename(obj.image.name)))
    image_tag.short_description = 'Image'

    def image_preview(self, obj):
        return format_html('<img src="/static/imgs/{}" style="max-height:300px; width:auto;" />'.format(os.path.basename(obj.image.name)))
    image_preview.short_description = 'Current Image'

    # Remove options that could break the gallery functionality
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Service, ServiceAdmin)
