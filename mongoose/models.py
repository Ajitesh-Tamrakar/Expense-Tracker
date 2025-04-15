from django.db import models

# Create your models here.
class raw_data(models.Model):
    sender = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)
    message_id = models.IntegerField()
    time = models.CharField(max_length=100)
    
# class Bank_data(models.Model):
#     bank = models.models.CharField(max_length=50)
#     pass
    
