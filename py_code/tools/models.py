# Create your models here.
# Response Body Models in Here
from django.db import models

class product(models.Model):
    id = models.AutoField(primary_key=True)
    no = models.CharField(max_length=20,blank=False) #no
    name = models.CharField(max_length=60,blank=True)
    comment = models.CharField(max_length=512,blank=True)
    code = models.CharField(max_length=256,blank=False)
    updateTime = models.DateTimeField(auto_now=True)
    creatTime = models.DateTimeField(auto_now_add=True)
    # Auth
    owner = models.ForeignKey('auth.User', related_name='product')
    highlighted = models.TextField()