# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from blogs.models import UserProfile

from mars.adapters import CustomAccountAdapter
from allauth.account.signals import user_signed_up
from django.contrib.auth.signals import user_logged_in


user = get_user_model()


@receiver(user_signed_up)
def handle_user_signed_up(request, sociallogin, user, **kwargs):
    
    # grab the user's data
    new_user_data = sociallogin.account.extra_data
    
    print(new_user_data)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print("Sender --> ", sender)
    print("Instance -->", instance)
    print("Created -->", created)
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try: 
        instance.profile.save() 
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=instance)
    
    
@receiver(user_logged_in)
def handle_user_login(sender, request, user, **kwargs):
    try:
        profile = user.profile
        profile.last_login_ip = request.META.get('REMOTE_ADDR') # Example: Store IP
        profile.save()
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=isinstance)
        print(f"Profile for user {user.username} does not exist.")

    # You can perform other actions here, like logging, updating session data, etc.
    
    
    
      