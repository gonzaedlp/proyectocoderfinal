from django.db import models

class User_profile(models.Model):
    user= models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone= models.CharField(max_length=20,blank=True)
    adress= models.CharField(max_length=200,blank=True)
    image= models.ImageField(upload_to='profile_image/',blank=True)