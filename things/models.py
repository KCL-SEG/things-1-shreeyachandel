from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=120, blank=True)
    quantity = models.IntegerField(default=0)

    def clean(self):
        if not 0 <= self.quantity <= 100:
            raise ValidationError("Quantity must be between 0 and 100.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
