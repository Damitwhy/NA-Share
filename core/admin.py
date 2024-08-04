from django.contrib import admin
from .models import Share, Comment, User

# Register the Share model with the admin site
admin.site.register(Share)
admin.site.register(Comment)
admin.site.register(User)