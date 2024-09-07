from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(max_length=200, blank=True)  # URL gambar produk
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)  # Rating produk
    time = models.DateField(auto_now_add=True)  # Data produk ditampilkan
    # feelings = models.TextField()
    # mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5

    def __str__(self):
        return self.name
