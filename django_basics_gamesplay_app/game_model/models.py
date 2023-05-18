from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
class Game(models.Model):
    CHOICES = (
        ("Action", "Adventure"),
        ("Puzzle", "Strategy"),
        ("Board/Card Game", "Board/Card Game"),
        ("Sports", "Other"),

    )
    title = models.CharField(max_length=30, blank=False, null=False, unique=True)
    category = models.CharField(max_length=15, choices=CHOICES, blank=False)
    rating = models.FloatField(blank=False, null=False, max_length=5, validators=[MinValueValidator(0.1)])
    max_level = models.IntegerField(blank=True, validators=[MinValueValidator(1)])
    image_url = models.URLField(blank=False, null=False)
    summary = models.TextField(blank=True)

