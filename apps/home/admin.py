from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
import os
import shutil
from django.conf import settings
from datetime import datetime
from .models import Photo, Service, Review, Promotion, TransformationVideo

# ====================== ADMIN ACTIONS & UTILITIES ======================
def backup_database(modeladmin, request, queryset):
    """Admin action to manually create a database backup."""
    backup_dir = "backups/"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{backup_dir}/backup_{timestamp}.db"
    shutil.copy2(settings.DATABASES['default']['NAME'], backup_path)
    messages.success(request, f"Backup created: {backup_path}")
backup_database.short_description = "🔒 Create DB Backup"

def restore_latest_backup(modeladmin, request, queryset):
    """Admin action to restore the latest backup."""
    backup_dir = "backups/"
    latest_backup = max(
        [os.path.join(backup_dir, f) for f in os.listdir(backup_dir) if f.endswith('.db')],
        key=os.path.getctime,
        default=None
    )
    if not latest_backup:
        messages.error(request, "No backups found!")
        return

    try:
        shutil.copy2(latest_backup, settings.DATABASES['default']['NAME'])
        messages.success(request, f"Restored from {latest_backup}!")
    except Exception as e:
        messages.error(request, f"Restore failed: {str(e)}")
restore_latest_backup.short_description = "🔄 Restore Latest Backup"

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'time_to_complete', 'description')
    search_fields = ('name', 'description')
    list_filter = ('cost', 'time_to_complete')
    actions = [backup_database, restore_latest_backup]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'link', 'stars')
    search_fields = ('title', 'text')
    actions = [backup_database, restore_latest_backup]
    
    paginate_by = 3  # Limit to 3 reviews per page
    empty_list = True


# PhotoAdmin class defined, inherits from admin.ModelAdmin
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag')
    search_fields = ('title',)
    readonly_fields = ('image_preview',)
    actions = [backup_database, restore_latest_backup]

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
    #def has_add_permission(self, request):
        #return False

    #def has_delete_permission(self, request, obj=None):
        #return False

    #def get_actions(self, request):
        #actions = super().get_actions(request)
        #if 'delete_selected' in actions:
            #del actions['delete_selected']
        #return actions
    
# New admin class for TransformationVideo model
class TransformationVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order', 'video_tag')
    search_fields = ('title', 'description')
    list_filter = ('order',)
    readonly_fields = ('video_preview',)
    actions = [backup_database, restore_latest_backup]
    
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Transformation Videos Administration'
        extra_context['subtitle'] = 'Manage your transformation videos. The videos will appear in the carousel in order of the "order" field.'
        return super(TransformationVideoAdmin, self).changelist_view(request, extra_context=extra_context)
    
    def video_tag(self, obj):
        video_basename = os.path.basename(obj.video.name)
        return format_html('''
            <video width="100" height="auto" controls>
                <source src="/static/videos/{}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        ''', video_basename)
    video_tag.short_description = 'Video'
    
    def video_preview(self, obj):
        video_basename = os.path.basename(obj.video.name)
        return format_html('''
            <video width="400" height="auto" controls>
                <source src="/static/videos/{}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        ''', video_basename)
    video_preview.short_description = 'Current Video'

#discountModal feature update
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'discount_percentage', 'start_date', 'end_date', 'message')
    search_fields = ('name', 'code')
    actions = [backup_database, restore_latest_backup]

admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(TransformationVideo, TransformationVideoAdmin)