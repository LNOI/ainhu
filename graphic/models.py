from django.db import models

# Create your models here.
class Logs(models.Model):
    history=models.CharField(blank=True,null=True,max_length=1000,default="x")