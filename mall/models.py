from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)