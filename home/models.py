from django.db import models

# Create your models here.

class Last_Projects(models.Model):
    photo = models.ImageField(upload_to='homeimage/')
    title = models.CharField(max_length=100)
    descrip = models.TextField(max_length=200)
    link = models.URLField(blank = True)

    def __str__(self):
        return self.title
