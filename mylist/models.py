from django.db import models
from django.conf import settings
from datetime import date
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Item(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    beschreibung = models.TextField(max_length=10000, default="")
    link = models.CharField(max_length=200, default="")
    public = models.CharField(max_length=200, default="")
    useridnummer = models.CharField(max_length=200, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    


    def __str__(self):
        #return self.title + ' | ' + self.author
        return str(self.id) + ' ' + self.name + ' | ' + str(self.author)