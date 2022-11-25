from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse



# Create your models here.

User = get_user_model()

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    beschreibung = models.TextField(max_length=10000, default="")
    link = models.CharField(max_length=200, default="", blank=True)
    CHOICES = (('public', 'public'),('private', 'private'),)
    public = models.CharField(max_length=7, choices=CHOICES)
    useridnummer = models.CharField(max_length=200, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)





    def __str__(self):
        #return self.title + ' | ' + self.author
        return str(self.id) + ' ' + self.name + ' | ' + str(self.author)


    def get_absolute_url(self):
        return reverse('mylist')



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.user)
