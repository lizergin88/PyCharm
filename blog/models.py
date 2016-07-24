from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Aritcle(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField
    user = models.ForeignKey(User)