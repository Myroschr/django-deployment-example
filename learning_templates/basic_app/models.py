from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    
    
    # Base that the user has alraedy account with her personal info
    # So with this way you will add new feature for this user
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING) 

    
    #addintional
    # parameter means that is not requred for the user
    portfolio_site = models.URLField(blank=True) 
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank=True)
    
    def _str__(self):
        return self.user.username