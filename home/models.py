from email.policy import default

from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=200)
    brandname = models.CharField(max_length=100,default="")
    contry = models.CharField(max_length=100,default="روژان")
    number=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    image = models.ImageField(blank = True,upload_to='product/')

# Create your models here.
