from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Post,Comment,UserProfile,Notification,ThreadModel,Tag

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['notification_type','to_user','from_user']

class ThreadModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','receiver']

class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name']


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(ThreadModel,ThreadModelAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Tag,TagAdmin)
