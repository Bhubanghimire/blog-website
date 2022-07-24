from django.db import models


# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="about")
    address = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    website = models.URLField()
