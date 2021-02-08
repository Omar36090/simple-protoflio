from django.db import models
from datetime import datetime

# Create your models here.
class blog(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blogimage/')
    descrip = models.TextField(max_length=1000)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
