from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)
    text_color = models.CharField(max_length = 100)
    background_color = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.CharField(max_length = 100)
    publish_date = models.DateTimeField(auto_now_add = True)
    categories = models.ManyToManyField(Category)
    author = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    