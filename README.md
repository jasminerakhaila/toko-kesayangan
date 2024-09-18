Nama : Jasmine Rakhaila

NPM : 2306165774

Kelas : PBP C

Tautan PWS : http://jasmine-rakhaila-tokokesayangan.pbp.cs.ui.ac.id/

Tautan Screenshot Postman: https://drive.google.com/drive/folders/12DEFDWkQZ8ff9KvLDJd21JMN4BbMjxz_?usp=sharing
 
 ### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawab: _Data delivery_ pada pengimplementasian sebuah platform merupakan fondasi untuk menjalankan fungsionalitas platform tersebut. _Data delivery_ memastikan bahwa informasi dari satu sistem dapat diteruskan ke sistem lain dengan cara yang terstruktur dan aman. Hal ini sangat penting untuk memastikan bahwa data yang relevan dapat diakses dan diproses oleh bagian sistem yang tepat pada waktu yang tepat dan efisien. Selain itu, _data delivery_ juga berperan penting dalam menjaga keamanan. Mereka memastikan bahwa data sensitif atau pribadi hanya dapat diakses oleh pihak yang berwenang. Dalam aspek operasional, _data delivery_ memastikan bahwa informasi yang diterima server dapat diproses lebih lanjut untuk berbagai tujuan seperti pengambilan keputusan, pembuatan laporan, hingga analitik. Dengan adanya _data delivery_ yang efektif, platform dapat memberikan layanan yang lebih responsif, aman, dan terintegrasi dengan baik, sehingga memberikan pengalaman pengguna yang optimal.

Sebagai kesimpulan, _data delivery_ merupakan komponen kunci yang mendukung aktivitas sebuah platform serta fungsi-fungsi penting dalam platform tersebut.

 ### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Jawab: Jika dibandingkan, JSON menampilkan data dalam bentuk key-value. Sedangkan, XML merepresentasikan data dalam bentuk pola pohon seperti format HTML.
```
JSON:
{"guests":[

  { "firstName":"John", "lastName":"Doe" },

  { "firstName":"Nikki", "lastName":"Wolf" }

]}

XML:
<guests>

  <guest>

    <firstName>John</firstName> <lastName>Doe</lastName>

  </guest>

  <guest>

    <firstName>María</firstName> <lastName>García</lastName>

  </guest>

  <guest>
```
Apabila dilihat secara sekilas, struktur JSON lebih mudah dibaca dibandingkan dengan XML yang terlalu bertele-tele.

Berikut penjabaran dari perbandingan utama JSON dan XML:
1. Penguraian: Ketika harus mengurai XML, diperlukan  pengurai XML yang sering kali memperlambat dan mempersulit proses. Sedangkan, mengurai JSON dapat menggunakan fungsi JavaScript standar. Fungsi ini lebih mudah diakses. Sehingga, kita dapat mengurai JSON dalam waktu yang lebih cepat daripada XML.
2. Kemudahan Penggunaan: Ukuran file JSON lebih kecil dan transmisi datanya lebih cepat dibandingkan dengan XML. File yang dihasilkan XML lebih kompleks untuk ditulis dan dibaca sehingga memakan banyak ruang.
3. Keamanan: 	
JSON lebih aman dibandingkan dengan XML. Hal ini dikarenakan XML rentan terhadap injeksi entitas eksternal (XXE) dan DTD yang tidak terstruktur. Sehingga kita perlu memastikan untuk menonaktifkan fitur DTD saat transmisi.

Sebagai kesimpulan, menurut saya JSON lebih baik dibandingkan XML dengan mempertimbangkan keamanan serta kemudahan dalam membaca file. Hal ini juga merupakan salah satu alasan JSON lebih populer karena lebih cepat dan efisien. Ditambah lagi, baris kode JSON yang jauh lebih sedikit daripada XML.

 ### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Jawab: Method is_valid() pada form Django digunakan untuk memvalidasi data yang diinput oleh pengguna melalui form. Hal ini digunakan untuk memastikan data tersebut sesuai aturan validasi sebelum disimpan atau diproses lebih lanjut. Method ini dibutuhkan untuk mencegah _logic error_ dalam aplikasi agar tidak salah tersimpan di database. Program akan menginformasikan pesan error ketika terjadi kegagalan validasi data. Sehingga, sebagai programmer akan mengetahui alasan adanya _invalid input data_ tersebut.

 ### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
 Kita membutuhkan `csrf_token` di Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). Tanpa `csrf_token`, penyerang dapat membuat halaman palsu yang, jika diakses oleh pengguna yang sudah masuk, bisa mengirimkan permintaan tidak sah ke aplikasi dengan menggunakan kredensial pengguna tersebut. Ini bisa menyebabkan perubahan data atau tindakan lain yang tidak diinginkan pada aplikasi.


 ### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 1. Membuat Input Form untuk Menambahkan Objek Model
Langkah pertama adalah membuat form untuk memasukkan data baru ke model yang ada. Saya akan membuat ModelForm di Django yang terhubung dengan model Product. Hal ini dilakukan dengan mendefinisikan form baru di forms.py, lalu mendefinisikan sebuah view di views.py untuk memproses form tersebut. View tersebut akan menampilkan form saat pengguna mengakses halaman dan akan memproses form jika pengguna mengirimkannya. Setelah itu, saya akan menambahkan template HTML yang berisi form, dan pada view-nya, jika data valid (dicek menggunakan form.is_valid()), maka data akan disimpan ke database menggunakan form.save().

2. Menambahkan Fungsi View untuk Menampilkan Data dalam Format XML dan JSON
Setelah form selesai dibuat, saya akan menambahkan fungsi view untuk menampilkan data dari model Product dalam format XML dan JSON. Untuk melakukan ini, saya akan menggunakan modul serialize dari django.core.serializers yang memungkinkan data model dikonversi menjadi format XML atau JSON. View ini akan mengambil semua data produk menggunakan Product.objects.all(), lalu menggunakan serialize() untuk mengubah data menjadi XML atau JSON. Hasilnya kemudian dikirim kembali sebagai HttpResponse dengan content type yang sesuai (application/xml atau application/json).

3. Menambahkan Fungsi View untuk Menampilkan Data Berdasarkan ID dalam Format XML dan JSON
Langkah berikutnya adalah menambahkan view tambahan untuk menampilkan data berdasarkan ID. Saya akan membuat view yang mirip dengan yang ada di langkah sebelumnya, tetapi kali ini mengambil data berdasarkan ID tertentu menggunakan Product.objects.get(id=<id>). Data yang diambil kemudian di-serialize menjadi XML atau JSON dan dikirim sebagai respons. Jika data dengan ID tersebut tidak ditemukan, saya akan mengembalikan status respons 404.

4. Membuat Routing URL untuk Setiap View
Langkah terakhir adalah menghubungkan semua view ke URL yang sesuai. Saya akan membuka file urls.py dan menambahkan routing baru untuk setiap view. Misalnya, URL /products/xml/ untuk menampilkan semua produk dalam format XML, dan /products/json/<id>/ untuk menampilkan produk berdasarkan ID dalam format JSON. Saya akan memastikan setiap URL memanggil view yang tepat, menggunakan pola seperti path('products/xml/', views.product_xml) atau path('products/json/<int:id>/', views.product_json_by_id).

Dengan langkah-langkah ini, saya dapat memastikan platform dapat menerima input data baru melalui form, serta menampilkan data dalam format XML dan JSON, baik secara keseluruhan maupun berdasarkan ID, sambil tetap menjaga struktur URL yang teratur.


 Referensi:
 https://docs.djangoproject.com/id/5.1/topics/forms/modelforms/
 https://aws.amazon.com/id/compare/the-difference-between-json-xml/
