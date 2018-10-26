from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.TextField(max_length=500, default="default.jpg")

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    post_content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="created")
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="updated")
    id_author = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return self.id

class Follow(models.Model):
    id_follower = models.IntegerField()
    id_followed = models.IntegerField()

class Hero(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=30, blank=False)
    playerClass = models.TextField(max_length=50, blank=False, default="NaN")

