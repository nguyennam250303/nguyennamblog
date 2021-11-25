from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(blank = True,null = True,upload_to = "images/")
    date = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.title + '|' + str(self.author)
