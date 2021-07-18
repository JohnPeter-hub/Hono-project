from django.contrib import admin
from .models import Post,Comment,UserProfile,Notification,ThreadModel

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['notification_type','to_user','from_user']

class ThreadModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','receiver']

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(ThreadModel,ThreadModelAdmin)
admin.site.register(Notification,NotificationAdmin)