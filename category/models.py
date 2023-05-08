from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)