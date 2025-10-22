# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from blogs.models import UserProfile
from allauth.account.signals import user_signed_up
from django.contrib.auth.signals import user_logged_in


@receiver(user_signed_up)
def handle_user_signed_up(request, sociallogin, user, **kwargs):
    
    # grab the user's data
    new_user_data = sociallogin.account.extra_data
    
    print(new_user_data)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    
@receiver(user_logged_in)
def handle_user_login(sender, request, user, **kwargs):
    try:
        profile = user.profile
        profile.last_login_ip = request.META.get('REMOTE_ADDR') # Example: Store IP
        profile.save()
    except UserProfile.DoesNotExist:
        # Handle cases where a profile might not exist (e.g., if created separately)
        print(f"Profile for user {user.username} does not exist.")

    # You can perform other actions here, like logging, updating session data, etc.
    