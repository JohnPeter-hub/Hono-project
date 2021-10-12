from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save,sender=User)
def addFollower(sender,instance,created, **Kwargs):
    if created:
        profile = UserProfile.objects.get(user=instance)
        profile.followers.add(instance)


