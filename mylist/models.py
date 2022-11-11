from django.db import models
from datetime import date

# Create your models here.
class ShoppingItem(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    beschreibung = models.TextField(max_length=10000, default="")
    link = models.CharField(max_length=200, default="")


    def __str__(self):
        return str(self.id) + ' ' + self.name