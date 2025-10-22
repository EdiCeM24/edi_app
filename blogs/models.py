from django.db import models, IntegrityError
from django.core.validators import MinLengthValidator, MaxValueValidator, EmailValidator
from django.utils.text import slugify
from django.contrib.auth.models import User      # this is the default user model or a single user model
# from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model   # this is the current user model


User = get_user_model()

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog')
    content = models.TextField()
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(args, **kwargs)
        
class BlogVid(models.Model):
    pass  


class UserProfile(models.Model):
     
        def clean(self):
           if not self.username.isalnum():
              raise ValidationError('Username should only contain alphanumeric characters.')
        
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=30, blank=True, null=True)
        location = models.CharField(max_length=200, blank=True, null=True)
        last_login_ip = models.GenericIPAddressField(blank=True, null=True)
        email = models.EmailField(
            max_length=25,
            validators=[EmailValidator],
            unique=True
        )
        password1 = models.CharField(
            max_length=12,
            validators=[MinLengthValidator(4)]
        )
        password2 = models.CharField(
            max_length=12,
            validators=[MinLengthValidator(4)]
        )
        
        def __str__(self):
            return self.user.username 

