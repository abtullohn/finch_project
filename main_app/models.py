from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sodas(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    flavor = models.CharField(max_length=500)
    verified_artist = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # Here is our new column
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']


# class (models.Model):

