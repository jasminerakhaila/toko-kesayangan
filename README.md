Nama : Jasmine Rakhaila

NPM : 2306165774

Kelas : PBP C

Tautan PWS : http://jasmine-rakhaila-tokokesayangan.pbp.cs.ui.ac.id/

# Tugas 6

### Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript memungkinkan aplikasi web menjadi interaktif dan dinamis, memberikan respons instan terhadap aksi pengguna tanpa perlu memuat ulang halaman. Dengan kemampuan asinkron seperti AJAX, JavaScript meningkatkan kecepatan dan efisiensi, memungkinkan komunikasi dengan server di latar belakang. Selain itu, JavaScript mendukung berbagai platform, memiliki integrasi yang mudah dengan HTML/CSS, dan didukung oleh banyak library dan framework untuk mempermudah pengembangan.

### Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi await dalam JavaScript digunakan untuk menunggu penyelesaian Promise, seperti yang dikembalikan oleh fetch(). Ketika menggunakan await dengan fetch(), eksekusi kode sementara dihentikan sampai Promise tersebut selesai, yang memungkinkan data yang di-fetch dapat digunakan seolah-olah operasi tersebut bersifat sinkron.

Jika kita tidak menggunakan await dengan fetch(), kode akan terus berjalan tanpa menunggu Promise dari fetch() terselesaikan. Hal ini berarti data yang diperlukan dari hasil fetch mungkin belum tersedia saat kita mencoba menggunakannya, yang bisa menyebabkan bugs atau kesalahan dalam mengelola state aplikasi karena kode akan berjalan sebelum data benar-benar siap.

### Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Decorator csrf_exempt digunakan pada view AJAX POST di Django untuk menonaktifkan pemeriksaan token CSRF. Hal ini biasanya dilakukan karena:

1. Integrasi Sistem Lain: Jika AJAX POST berasal dari sumber atau domain yang tidak bisa mengirim token CSRF.
2. Kemudahan Pengembangan: Untuk menghindari pengelolaan token CSRF selama pengembangan awal.
3. API untuk Non-Browser Client: Ketika endpoint dimaksudkan untuk digunakan oleh klien non-browser yang tidak memerlukan proteksi CSRF.

Penggunaan csrf_exempt harus hati-hati karena mengurangi keamanan aplikasi terhadap serangan CSRF.


### Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data di backend menjadi sangat penting karena bertindak sebagai lapisan keamanan tambahan. Apabila ada celah atau kelemahan pada sisi frontend, seperti pengguna yang sengaja melewati validasi frontend atau menggunakan script untuk mengirimkan data secara langsung ke server, maka pembersihan dan validasi di backend akan menghalangi data yang tidak sesuai atau berbahaya tersebut dari masuk ke sistem. Ini membantu dalam mencegah berbagai serangan seperti SQL Injection atau Cross-Site Scripting yang bisa terjadi jika input dari pengguna tidak divalidasi atau dibersihkan secara efektif. Selain itu, proses ini juga memastikan konsistensi data yang diterima dari berbagai sumber dan pengguna yang berbeda.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. Membuat Endpoint untuk AJAX GET:
Saya telah membuat view di Django yang bertanggung jawab hanya untuk menampilkan data produk pengguna yang telah login, menggunakan sesi pengguna yang aktif sebagai filter.

2. Mengambil Data Produk dengan AJAX GET: 
Saya menggunakan JavaScript untuk memanggil data produk dari endpoint yang dibuat. Fungsi fetch digunakan untuk mendapatkan data secara asinkron, yang kemudian saya tampilkan di halaman tanpa perlu memuat ulang.

3. Menambahkan Produk dengan AJAX POST: 
- Saya menyiapkan sebuah modal yang berisi form untuk menambahkan produk baru. Form ini mencakup input untuk nama produk, harga, deskripsi, dan rating.
- Modal diaktifkan oleh sebuah tombol di halaman utama. Setelah pengguna mengisi form dan menekan submit, JavaScript mengirim data tersebut ke server melalui AJAX POST.

4. Menangani Keamanan Data Form: 
- Untuk mencegah XSS, saya memastikan bahwa semua input dari form disanitasi pada sisi server sebelum disimpan ke database.
- Saya juga menerapkan escape secara hati-hati pada output yang dikembalikan ke halaman HTML, menghindari potensi eksekusi skrip berbahaya yang mungkin disisipkan melalui input yang tidak terkontrol.

5. Memperbarui Halaman Secara Dinamis: 
Setelah produk berhasil ditambahkan, form di modal dibersihkan, modal ditutup, dan saya memperbarui daftar produk yang ditampilkan di halaman utama secara dinamis menggunakan JavaScript untuk merefleksikan perubahan tanpa perlu memuat ulang halaman.

6. Menampilkan Pesan Kesalahan: 
Jika ada kegagalan dalam menambahkan produk baru (misalnya, karena validasi server), saya menampilkan pesan kesalahan di dalam modal untuk memberikan umpan balik kepada pengguna.