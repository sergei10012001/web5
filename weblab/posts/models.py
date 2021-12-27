from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField('Title', max_length=50, default="Title")
    text = models.TextField('Text')

    def get_absolute_url(self):
        return f'/posts/{self.id}'

    def __str__(self):
        return self.title
