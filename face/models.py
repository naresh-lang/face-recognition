from django.db import models

# Create your models here.

class Registration(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    mobile=models.IntegerField()
    image = models.FileField(blank=True, default='album_logos/no-image.jpg')

 