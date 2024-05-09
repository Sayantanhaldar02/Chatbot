from django.db import models

# Create your models here.
class Chatbot(models.Model):
    user_input = models.CharField(max_length=2000, null=True,blank=True)
    response= models.CharField(max_length=2000, null=True,blank=True)