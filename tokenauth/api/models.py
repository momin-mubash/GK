from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

#we are writing this code here bcoz this file start excecuting first just after start before views.py file 
#this is a signal which are used to generate token automatically when user is created
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save,sender=settings.AUTH_USER_MODEL)#due to post_save signal after user is saved this signal will be trigerred
def create_auth_token(sender , instance=None , created=False , **kwargs):
    if created:
        Token.objects.create(user=instance)
