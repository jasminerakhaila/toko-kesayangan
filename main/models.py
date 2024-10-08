from django.db import models
import uuid  # tambahkan baris ini di paling atas
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    # image_url = models.URLField(max_length=200, blank=True)  # URL gambar produk
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)  # Rating produk
    time = models.DateField(auto_now_add=True)  # Data produk ditampilkan
   

    def __str__(self):
        return self.name
