from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    email = models.EmailField(blank=False, null=False)
    age = models.IntegerField(blank=False, validators=[MinValueValidator(12)])
    password = models.CharField(max_length=30, blank=False, null=False)
    first_name = models.CharField(blank=True, max_length=30)
    last_name = models.CharField(blank=True, max_length=30)
    profile_picture = models.URLField(blank=True)
