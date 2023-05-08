from django.db import models
from sub_category.models import SubCategory


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=250)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=False)
