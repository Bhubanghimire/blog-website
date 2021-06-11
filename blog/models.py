from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='images/user/', blank=True, null=True)
    
class Category(models.Model):
    category=models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Post(models.Model):
    title=models.CharField(max_length=200,default="")
    post = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='images/post/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    created_date =  models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    