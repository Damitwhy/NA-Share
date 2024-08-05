from django.contrib import admin
from .models import Share, Comment, User, Message
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import messages

# Register the Share model with the admin site
admin.site.register(Share, SummernoteModelAdmin)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Message)

def show_messages(modeladmin, request, queryset):
    for obj in queryset:
        messages.info(request, f"Message for {obj}")
show_messages.short_description = "Show Messages"

admin.site.add_action(show_messages)