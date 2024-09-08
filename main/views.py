from itertools import product
from django.shortcuts import render
from main.models import Product

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306165774',
        'name': 'Jasmine Rakhaila',
        'class': 'PBP C',
        'nama_toko' : 'Toko Kesayangan'
    }

    return render(request, "main.html", context)


def product_list(request):
    products = Product.objects.all()  # Mengambil semua produk dari database
    context = {
        'products': products  # Mengirim data produk ke template
    }
    return render(request, 'main.html', context)
