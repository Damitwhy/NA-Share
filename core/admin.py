from django.contrib import admin
from .models import Share, Comment, User
from django_summernote.admin import SummernoteModelAdmin

# Register the Share model with the admin site
admin.site.register(Share, SummernoteModelAdmin)
admin.site.register(Comment)
admin.site.register(User)