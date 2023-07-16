from django.db import models
type = (
    ("technology", "Technology"),
    ("fashion", "Fashion"),
    ("healthbeauty", "Health and Beauty"),
    ("toy", "Toy"),
    ("fitness", "Fitness"),
    ("food", "Food"),
)
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    kind = models.CharField(max_length = 100, choices = type, default="technology")
    cost = models.IntegerField()

