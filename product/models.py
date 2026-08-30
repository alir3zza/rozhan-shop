from itertools import product
from symtable import Class

from django.db import models

# Create your models here.
from django.db import models

class Products(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    explane = models.CharField(max_length=100)
    image = models.ImageField(upload_to="product/", default="")

