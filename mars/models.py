from django.db import models
from django.db.utils import DatabaseError
from django.db import connection
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator, MaxValueValidator
from django.contrib.auth.models import User      # this is the default user model or a single user model
from django.contrib.auth import get_user_model   # this is the current user model
import uuid




class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"

  
class Users(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    
    
class About(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='picture', blank=True, null=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class AboutDelivery(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
    
class AboutSwipe(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='resource', blank=True, null=True)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=100, validators=[MinLengthValidator(3), MaxValueValidator(100)], blank=True, null=True) 
    last_name = models.CharField(max_length=100, validators=[MinLengthValidator(3), MaxValueValidator(100)], blank=True, null=True) 
    email = models.EmailField(max_length=30, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9, 18}$', message="Phone number must be entered in the format: '+234 803 099 9999'. Up to 15 digits is allowed.")
    phone_number = PhoneNumberField(validators=[phone_regex], max_length=15, blank=False)
    subject = models.CharField(max_length=50, validators=[MinLengthValidator(5), MaxValueValidator(50)])
    website = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(validators=[MinLengthValidator(3), MaxValueValidator(300)])
    
  
                
    
    def __str__(self):
        return self.first_name    
    
      
class Feed_back(models.Model):
    name = models.CharField(max_length=100, default='')
    msg = models.TextField(validators=[MinLengthValidator(15), MaxValueValidator(500)],)
    
    def __str__(self):
        return self.name
        
    
class Portfolio(models.Model):
    caption = models.CharField(max_length=255)    
    image = models.ImageField(upload_to='app', blank=True, null=True)
    text = models.CharField(max_length=255)
    readMore = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    
    
class PortfolioVideo(models.Model):
    caption = models.CharField(max_length=255)    
    image = models.FileField(upload_to='video', blank=True, null=True)
    text = models.CharField(max_length=255)
    readMore = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    
    
class PortfolioDetail(models.Model):
    continue_text = models.CharField(max_length=255, blank=True, null=True)
    head_word = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField(max_length=300, blank=True, null=True)
    display_image = models.ImageField(upload_to='gallery', blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.continue_text
    
class PortVideo(models.Model):
    title = models.CharField(max_length=255, default="")
    continue_from_prev = models.CharField(max_length=100, default='')
    video = models.FileField(upload_to='res', default='', blank=True, null=True)
    text = models.TextField(max_length=500, default='')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Services(models.Model):
    title = models.CharField(max_length=255)    
    image = models.ImageField(upload_to='store', blank=True, null=True)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class Skill(models.Model):
    name = models.CharField(max_length=200)
    numInPercentage = models.IntegerField()
     
    def __str__(self):
        return self.name   
    

class Term(models.Model):
    caption = models.CharField(max_length=255, default="")
    message = models.TextField(max_length=500, default="")
    image = models.FileField(upload_to='uploads', default="")
    author = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='Edi_Mars')
    created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.caption 


class Privacy_policy(models.Model):
    title = models.CharField(max_length=255, default="")
    text_msg = models.TextField(max_length=500, default="")
    image = models.FileField(upload_to='shop', default="")
    author = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='Edidiong')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name 

