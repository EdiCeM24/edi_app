from django.db import models


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
    
    