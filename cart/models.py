from django.db import models
from store.models import Product, Image

# Create your models here.

class CartItem(models.Model):
    session_key = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
    
