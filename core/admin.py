from django.contrib import admin
from .models import User, Message, Share, Comment, ContactMessage, VisitorCount
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import messages

# visitor count admin
class VisitorCountAdmin(admin.ModelAdmin):
    list_display = ('id', 'count')
    readonly_fields = ('id', 'count')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(VisitorCount, VisitorCountAdmin)

# Define an admin action to show messages
def show_messages(modeladmin, request, queryset):
    for obj in queryset:
        messages.info(request, f"Message for {obj}")

show_messages.short_description = "Show Messages"

# Register existing models
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Share, SummernoteModelAdmin)
admin.site.register(Comment)

# Register the ContactMessage model
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

# Add the custom admin action
admin.site.add_action(show_messages)

def is_admin_or_superuser(user):
    return user.is_authenticated and (user.is_superuser or user.is_staff)