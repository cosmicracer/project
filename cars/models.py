from django.db import models

# Create your models here.

class work(models.Model):
    name=models.CharField(max_length=20,default="")
    mail=models.CharField(max_length=40,default="")
    inbox=models.CharField(max_length=50,default="")

class restore(models.Model):
    name=models.CharField(max_length=20, default="")
    mail=models.EmailField(max_length=40, default="")
    inbox=models.CharField(max_length=50, default="")

class buy(models.Model):
    name=models.CharField(max_length=20,default="")
    mail=models.EmailField(max_length=40,default="")
    inbox=models.CharField(max_length=50, default="")

