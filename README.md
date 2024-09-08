Nama : Jasmine Rakhaila

NPM : 2306165774

Kelas : PBP C

Tautan PWS : TBA

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
Jawab:  Untuk memulai seluruh step, saya membuat repositori baru di github bernama toko-kesayangan. Saya juga membuat direktori lokal di laptop yang juga bernama toko-kesayangan yang telah diinisiasi git.

**Pembuatan Proyek Django Baru**
1. Pada terminal toko-kesayangan, langkah pertama yang saya lakukan ialah membuka terminal dan membuat *virtual environment* dengan menjalankan "python3 -m venv env" dan "source env/bin/activate" untuk mengaktifkan *virtual environment*. 
2. Lalu, saya menginstall beberapa *dependencies* yang disimpan dalam file requirements.txt: django, gunicorn, whitenoise, psycopg2-binary, requests, urllib3. *Dependencies* tersebut digunakan agar proyek dapat berfungsi dengan benar. Instalasi dilakukan dengan menjalankan "pip install -r requirements.txt".
3. Langkah terakhir yaitu saya membuat proyek Django bernama toko_kesayangan dengan menjalankan "django-admin startproject toko_kesayangan ." pada terminal. Nantinya, akan tercipta sebuah file bernama "manage.py".

**Pembuatan Aplikasi Main Pada Proyek toko_kesayangan**

1. Langkah pertama yaitu saya menuju pada terminal toko-kesayangan dengan menjalankan cd [path toko-kesayangan]. 
2. Lalu, saya mengaktifkan *virtual environment* terlebih dahulu dengan menjalankan "source env/bin/activate".
3. Untuk membuat aplikasi main, saya menjalankan perintah "python manage.py startapp main" pada terminal. Direktori main telah terbentuk yang berisi struktur awal pembuatan proyek django toko-kesayangan.
4. Terakhir, saya mendaftarkan aplikasi main ke dalam proyek. Caranya dengan menambahkan 'main' ke dalam daftar INSTALLED_APPS di file settings.py, yang terbentuk saat pembuatan proyek Django.

**Routing pada Proyek toko_kesayangan**
1. Langkah pertama yaitu saya membuka file urls.py pada proyek toko_kesayangan. 
2. Lalu, saya menambahkan kode berikut di dalam file urls.py

```from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

3. Fungsi "from django.urls import path, include" digunakan untuk mengimpor rute URL dari aplikasi main ke dalam berkas urls.py toko_kesayangan.

**Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib: nama, price, description**
Pada file models.py pada aplikasi main, saya meng-import models dari django.db. Lalu, saya membuat class Product yang berparameter models.Model. Ini berfungsi untuk mendefinisikan model database di Django, di mana setiap atribut dalam class ini akan menjadi kolom dalam tabel database.
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(max_length=200, blank=True)  # URL gambar produk
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)  # Rating produk
    time = models.DateField(auto_now_add=True) # Date added product 

    def __str__(self):
        return self.name

```
 
 **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**


### **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
<br />Jawab:

**Jelaskan fungsi git dalam pengembangan perangkat lunak!**
<br />Jawab:


**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
<br />Jawab:

**Mengapa model pada Django disebut sebagai ORM?**
<br />Jawab:
