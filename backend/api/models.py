from django.db import models
from datetime import datetime

class Car(models.Model):
    COLOUR_CHOICES = [
        ("red", "Red"),
        ("blue", "Blue"),
        ("green", "Green"),
        ("black", "Black"),
    ]
    name = models.CharField(max_length = 200)
    year = models.IntegerField(default=datetime.now().year)
    colour = models.CharField(max_length=10, choices=COLOUR_CHOICES, default="black")
    miles_driven = models.IntegerField(default=0)
    multimedia = models.BooleanField(default=True)


    def __str__(self):
        return self.name
