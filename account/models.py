from django.db import models
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.TextField()
    avatar = models.ImageField(upload_to="avatar/")

    def __str__(self):
        return super().user.username

# Create your models here.

