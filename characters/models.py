from django.db import models
from django.urls import reverse
from accounts.models import CustomUser


# Create your models here.
class Character(models.Model):
    name: models.ForeignKey.CharField(max_length=120)
    description= models.TextField(blank=True, null=True)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('characters-list')