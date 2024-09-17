Nama : Jasmine Rakhaila

NPM : 2306165774

Kelas : PBP C

Tautan PWS : http://jasmine-rakhaila-tokokesayangan.pbp.cs.ui.ac.id/
 
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


 ### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).


 Referensi:
 https://docs.djangoproject.com/id/5.1/topics/forms/modelforms/
 https://aws.amazon.com/id/compare/the-difference-between-json-xml/
