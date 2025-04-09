from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


class Skill(models.Model):
    name = models.CharField(max_length=200)
    numInPercentage = models.IntegerField()
     
    def __str__(self):
        return self.name
    
    
class About(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='picture', blank=True, null=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Portfolio(models.Model):
    caption = models.CharField(max_length=255)    
    image = models.ImageField(upload_to='app', blank=True, null=True)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Services(models.Model):
    title = models.CharField(max_length=255)    
    image = models.ImageField(upload_to='store', blank=True, null=True)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class SignupForm(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return self.name    
    
    
class Contact(models.Model):
    fname = models.CharField(max_length=100, blank=True, null=True) 
    lname = models.CharField(max_length=100, blank=True, null=True) 
    username = models.CharField(max_length=40)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9, 15}$', message="Phone number must be entered in the format: '+23480309999999'. Up to 15 digits is allowed.")
    phone_number = PhoneNumberField(validators=[phone_regex], max_length=15, blank=False)
    subject = models.CharField(max_length=50)
    website = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    company_name = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name    
    
    