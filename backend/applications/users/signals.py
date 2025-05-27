from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models.user_profile import UserProfile

User = get_user_model()


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
