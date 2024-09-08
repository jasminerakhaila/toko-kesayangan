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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

3. Fungsi "from django.urls import path, include" digunakan untuk mengimpor rute URL dari aplikasi main ke dalam berkas urls.py toko_kesayangan.

**Membuat Model pada Aplikasi Main Bernama Product dan Memiliki Atribut: nama, price, description**

Pada file models.py pada aplikasi main, saya meng-import models dari django.db. Lalu, saya membuat class Product yang berparameter models.Model. Ini berfungsi untuk mendefinisikan model database di Django, di mana setiap atribut dalam class ini akan menjadi kolom dalam tabel database.
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255) # Nama Produk
    price = models.IntegerField() # Harga Produk
    description = models.TextField() # Deskripsi Produk
    image_url = models.URLField(max_length=200, blank=True)  # URL gambar produk
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)  # Rating produk
    time = models.DateField(auto_now_add=True) # Tanggal produk ditambahkan  

    def __str__(self):
        return self.name

```
 
 **Membuat Sebuah Fungsi pada views.py untuk Dikembalikan ke Dalam Sebuah Template HTML yang Menampilkan Nama Aplikasi serta Nama dan Kelas**
1. Pada views.py pada aplikasi main, saya membuat fungsi show_main untuk menyimpan dictionary yang berisi key dan value. Key ini akan dipanggil di template HTML, sementara value berisi data yang akan ditampilkan.
```
from django.shortcuts import render
from main.models import Product

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306165774',
        'name': 'Jasmine Rakhaila',
        'class': 'PBP C',
        'store_name' : 'Toko Kesayangan'
    }

    return render(request, "main.html", context) 
    # penjelasan parameter: (permintaan HTTP pengguna, template HTML yang digunakan, data yang akan diproses dan ditampilkan pada HTML)

# Fungsi untuk menampilkan database produk    
def product_list(request):
    products = Product.objects.all()  # Mengambil semua produk dari database
    context = {
        'products': products  # Mengirim data produk ke template
    }
    return render(request, 'main.html', context)

```
2. from django.shortcuts import render: Fungsi ini digunakan untuk merender (menyusun) template HTML dengan context data yang akan ditampilkan ke pengguna. 
3. from main.models import Product: Mengimpor model Product dari file models.py yang berada di aplikasi main. Model ini digunakan untuk mengambil data produk dari database.
4. Berikut template HTML yang saya buat untuk menampilkan nama aplikasi, nama, dan kelas.
```
<html>
<head>
    <!-- Menautkan file CSS -->
    <link rel="stylesheet" type="text/css" href="{% static 'templates/main.css' %}">  # Belum dipakai
</head>
<body>
<div class="info-container">
  <div class="info-item">
    <h5>NPM: {{ npm }}</h5>
  </div>
  <div class="info-item">
    <h5>Name: {{ name }}</h5>
  </div>
  <div class="info-item">
    <h5>Class: {{ class }}</h5>
    <h1>Welcome to {{store_name}}!</h1>
  </div>
</div>
</body>

# Pembuatan lanjutan HTML khusus penampilan produk dapat dilihat di repositori github

```
5. Pemanggilan key dilakukan dengan menggunakan double bracket {{...}}, yang berfungsi untuk menampilkan data dari context pada template HTML di Django.

**Routing pada urls.py Aplikasi Main untuk Memetakan Fungsi yang Telah Dibuat pada views.py**
1. Langkah pertama yang saya lakukan adalah membuat urls.py dalam direktori main.
2. Kemudian, saya mengisi urls.py dengan kode berikut
```
from django.urls import path  # Mengimpor fungsi path untuk mendefinisikan pola URL.
from main.views import show_main # function show_main ditampilkan ketika URL terkait diakses.
from . import views  # Mengimpor modul views dari direktori saat ini.

app_name = 'main'  # Mendefinisikan namespace aplikasi sebagai 'main'.

urlpatterns = [
    # Mengarahkan URL root ('') ke fungsi show_main dan memberi nama 'show_main'.
    path('', views.show_main, name='show_main'), 
]
```
**Deployment ke PWS**
1. Setelah melakukan login akun PWS, saya membuat proyek baru bernama "tokokesayangan". 
2. Lalu, saya menyimpan *Project Credentials* dan *Project Command* untuk keperluan login username dan password yang akan diminta oleh terminal.
3. Pada settings.py di proyek Django toko_kesayangan, saya menambahkan URL deployment PWS pada ALLOWED_HOSTS.

```
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "jasmine-rakhaila-tokokesayangan.pbp.cs.ui.ac.id"]

```
Langkah ini dilakukan agar proyek Django toko_kesayangan dapat diakses melalui URL deployment PWS.

### **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
Jawab: Berikut bagan yang dapat diakses https://drive.google.com/file/d/1vCMEF_npQ4dwmRtxpgI6GQ0o7T-kZ-uy/view?usp=sharing

Penjelasan: 
1. Client Request: Pengguna mengakses URL di browser dan mengirimkan permintaan ke server Django. Permintaan ini bisa berupa halaman web atau data.

2. urls.py: Django memproses request dengan mencocokkannya ke pola URL di urls.py, lalu mengarahkannya ke fungsi yang tepat di views.py.

3. views.py: views.py menjalankan logika aplikasi, memproses data, atau berinteraksi dengan database jika diperlukan melalui models.py.

4. models.py: models.py berkomunikasi dengan database untuk mengambil atau menyimpan data yang dibutuhkan oleh views.py.

5. HTML Template: Data dari views.py dirender ke dalam template HTML, sehingga menghasilkan halaman web yang siap ditampilkan.

6. Client Response: Django mengirimkan halaman web yang dirender kembali ke browser untuk ditampilkan kepada pengguna.

Keterkaitan antara urls.py, views.py, models.py, dan berkas html:
- urls.py berfungsi sebagai pengarah request ke views.py.
- views.py menjalankan logika aplikasi dan, jika diperlukan, meminta data dari models.py yang berhubungan dengan database.
- models.py mengelola data yang diminta oleh views.py dan mengirimkan kembali hasilnya.
- Setelah itu, views.py menggunakan berkas HTML (template) untuk merender tampilan data dan mengirimkannya kembali sebagai respon ke client.

### **Jelaskan fungsi git dalam pengembangan perangkat lunak!**
Jawab: Git adalah alat yang digunakan oleh pengembang dan programmer sebagai sistem kontrol untuk pengembangan perangkat lunak. Tujuan utama penggunaan Git adalah untuk mengelola versi kode sumber program, yang memungkinkan pengaturan baris dan kode yang akan ditambahkan atau diubah. 
Adapun fungsi git dalam pengembangan perangkat lunak:

- Kolaborasi: Git digunakan banyak pengembang untuk bekerja pada proyek yang sama secara bersamaan. Fitur ini mendukung kolaborasi tim dengan memungkinkan penggabungan kontribusi dari berbagai anggota tim, meskipun mereka bekerja secara terpisah. Kemudian  pekerjaan atau perubahan diintegrasikan ke dalam proyek utama dengan cara yang terkoordinasi dan teratur.

- Organisasi Proyek: Git membantu dalam mengorganisir proyek dengan mengelompokkan versi kode dalam folder atau cabang seperti V1, V2, V3, dan seterusnya. Setiap versi kode yang disimpan di dalam Git dapat diakses kapan saja. Ini memudahkan manajemen berbagai versi file proyek dan memungkinkan pengembang untuk melacak perubahan dari satu versi ke versi lainnya dengan mudah.

- Proyek Open Source: Git dimanfaatkan pengembang untuk berkolaborasi secara terbuka dan berbagi kode sumber dengan komunitas luas. Hal ini dapat mempercepat inovasi dan memungkinkan kontribusi dari berbagai pihak.

- Fleksibilitas: Git juga berfungsi sebagai platform hosting yang fleksibel dengan berbagai layanan seperti GitLab, GitHub, Bitbucket, dan SourceForge. Platform-platform ini menawarkan berbagai fitur untuk manajemen proyek, pelacakan bug, integrasi dengan alat lain, dan otomatisasi proses pengembangan. 

- Backup dan Pemulihan: Git berfungsi sebagai mekanisme cadangan (backup) dengan menyimpan riwayat versi kode secara lengkap. Jika terjadi masalah atau kesalahan pada versi terbaru, Git mengembalikan kode ke versi sebelumnya. Hal ini meminimalkan risiko kehilangan data dan memfasilitasi pemulihan yang efektif.


### **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
Jawab: Django sering dipilih sebagai framework awal dalam pembelajaran pengembangan perangkat lunak. Hal ini karena Django menyediakan fitur lengkap yang bisa dipakai oleh pengembangan aplikasi web dengan berbagai kemampuan, tanpa memerlukan alat eksternal. Framework ini menawarkan dokumentasi yang komprehensif serta tutorial yang memudahkan pemula memahami konsep dan praktik terbaik dalam pengembangan. Struktur terorganisir Django, dengan pemisahan model, tampilan, dan template (MTV) membantu pemula membangun aplikasi web dengan cara yang terstruktur dan bersih. Selain itu, Django dilengkapi dengan fitur keamanan bawaan yang melindungi aplikasi dari berbagai ancaman serta didukung oleh komunitas aktif yang memudahkan pencarian bantuan. Meskipun cocok untuk pemula, Django juga digunakan dalam proyek skala besar, sehingga memberikan fondasi yang kuat untuk pengembangan berkelanjutan.

### **Mengapa model pada Django disebut sebagai ORM?**
Jawab: Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena fungsinya adalah menjembatani antara database relasional dan kode berbasis objek. ORM membantu pengembang untuk berinteraksi dengan database menggunakan bahasa pemrograman Python tanpa harus menulis query SQL secara langsung. Dengan menggunakan ORM, pengembang dapat melakukan operasi pada database secara lebih intuitif. ORM secara otomatis menerjemahkan operasi tersebut ke dalam SQL yang sesuai. Hal ini mempermudah manajemen data dan membuat kode lebih bersih dan mudah dipelihara.