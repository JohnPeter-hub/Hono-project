from django.contrib import admin
from .models import Post,Comment,UserProfile,Notification

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['notification_type','to_user','from_user']

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Notification,NotificationAdmin)