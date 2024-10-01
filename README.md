Nama : Jasmine Rakhaila

NPM : 2306165774

Kelas : PBP C

Tautan PWS : http://jasmine-rakhaila-tokokesayangan.pbp.cs.ui.ac.id/

# Tugas 5

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Urutan prioritas dalam pengambilan CSS selector sangat penting dalam menentukan gaya yang akan diterapkan pada elemen HTML. Prioritas ini ditentukan berdasarkan beberapa faktor seperti kekhususan (specificity), keberadaan inline styles, dan urutan kode CSS itu sendiri. Berikut adalah urutan prioritas pengambilan CSS selector yang umum digunakan:

1. Inline Styles: Gaya yang didefinisikan langsung dalam atribut style elemen HTML memiliki prioritas tertinggi. Ini karena inline styles dianggap paling spesifik karena secara langsung terikat dengan elemen tersebut.
2. ID Selectors: Selector yang menggunakan ID (#id) memiliki prioritas yang lebih tinggi berikutnya. ID unik untuk setiap elemen pada halaman, sehingga definisi gaya yang menggunakan ID sangat spesifik.

3. Class, Pseudo-class, dan Attribute Selectors: Selector yang menggunakan class (.class), pseudo-class (:hover, :focus, dll.), dan attribute selectors ([type="text"]) memiliki prioritas lebih rendah dari ID selectors tetapi lebih tinggi dari tag selectors. Selector ini cukup spesifik dan sering digunakan untuk menentukan gaya berdasarkan kelompok elemen atau keadaan elemen.

4. Tag (Type) Selectors: Selector yang menggunakan nama tag (div, p, a, dll.) memiliki prioritas yang lebih rendah karena merupakan gaya yang paling umum dan dapat diterapkan ke banyak elemen sekaligus.

5. Universal Selector: Universal selector (*), yang berlaku untuk semua elemen, memiliki prioritas paling rendah. Selector ini sering digunakan untuk mengatur nilai default dari properti tertentu sebelum selektor yang lebih spesifik diterapkan.

6. (!important): Properti yang menggunakan deklarasi !important akan memiliki prioritas lebih tinggi dari selektor biasa, meskipun ini sebaiknya digunakan dengan hati-hati karena bisa membuat CSS menjadi sulit untuk dipelihara dan debug.

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design merupakan konsep penting dalam pengembangan aplikasi web karena memastikan bahwa sebuah situs web dapat diakses dan ditampilkan dengan baik di berbagai perangkat dan ukuran layar. Dengan bertambahnya penggunaan perangkat mobile untuk mengakses internet, situs web yang responsif menjadi krusial untuk menjangkau audiens yang lebih luas. 

Twitter adalah contoh dari aplikasi web yang telah menerapkan responsive design. Ketika diakses melalui berbagai perangkat agar tetap fungsional dan estetis. Layout responsif ini memastikan bahwa semua elemen seperti feed, tombol, dan menu navigasi dapat diakses dengan mudah dan tampak harmonis di berbagai ukuran layar.

Contoh website yang belum menerapkan responsive design adalah siasisten.cs.ui.ac.id. Website ini belum menyediakan tampilan untuk mobile device, melainkan hanya desktop view. 


### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Margin, border, dan padding adalah tiga properti penting dalam CSS yang digunakan untuk mengatur tata letak elemen di halaman web. Margin adalah ruang kosong di luar elemen, yang berfungsi untuk memberikan jarak antara elemen dengan elemen lain di sekitarnya. Margin tidak mempengaruhi ukuran elemen itu sendiri. Implementasinya sederhana, cukup menggunakan properti margin di CSS, seperti margin: 20px; untuk memberikan jarak 20 piksel di semua sisi elemen.

Border adalah garis pembatas yang mengelilingi elemen dan berada di antara margin dan padding. Border dapat diatur ketebalannya, jenis garisnya, serta warnanya, misalnya dengan kode border: 2px solid black; yang membuat garis pembatas berukuran 2 piksel, tipe solid, dan berwarna hitam. Border memberikan efek visual pada elemen tanpa mempengaruhi margin atau padding, tetapi akan menambah ukuran elemen.

Padding adalah ruang di dalam elemen, antara konten dan border elemen. Padding menambah ruang internal sehingga konten tidak terlalu menempel pada border. Misalnya, dengan padding: 10px; akan menambahkan ruang 10 piksel di dalam elemen di semua sisinya. Berbeda dengan margin, padding menambah ukuran keseluruhan elemen karena menjadi bagian dari area konten yang diperluas.

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox dan Grid Layout adalah dua sistem tata letak dalam CSS yang digunakan untuk menyusun elemen secara responsif dan fleksibel. Flexbox (Flexible Box) bekerja secara satu dimensi, baik secara horizontal (row) maupun vertikal (column), dan sangat berguna untuk mengatur elemen dalam satu baris atau kolom. Dengan Flexbox, elemen dapat secara otomatis menyesuaikan ukuran atau posisi berdasarkan ruang yang tersedia, misalnya dengan properti seperti justify-content, align-items, dan flex-wrap. Ini sangat bermanfaat untuk tata letak yang sederhana dan dinamis, seperti navigasi atau susunan kartu produk.

Di sisi lain, Grid Layout bekerja secara dua dimensi, memungkinkan pengaturan elemen secara simultan dalam baris (rows) dan kolom (columns). Grid lebih cocok digunakan untuk tata letak yang lebih kompleks seperti halaman utama atau layout blog, di mana Anda dapat mendefinisikan ukuran kolom dan baris secara presisi dengan properti seperti grid-template-rows dan grid-template-columns. Flexbox lebih baik untuk elemen tunggal atau satu dimensi, sedangkan Grid lebih unggul dalam pengaturan tata letak yang lebih komprehensif dan simetris.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Untuk memaparkan secara detail bagaimana saya telah mengimplementasikan checklist pada proyek pengembangan web, berikut adalah langkah-langkah yang saya lakukan:

1. Pengembangan Fungsi Backend:
- Untuk menghapus produk, saya menambahkan sebuah route pada backend yang menerima permintaan DELETE. Fungsi ini bertugas menghapus produk berdasarkan ID yang diterima dari front-end. Saya memastikan bahwa operasi ini hanya dapat dilakukan oleh pengguna yang terotentikasi dan berhak atas aksi tersebut.
- Untuk mengedit produk, saya membuat route yang menerima permintaan POST. Fungsi ini mengambil data yang diinputkan melalui form edit produk dan melakukan pembaruan pada database sesuai dengan ID produk. Saya menggunakan validasi data untuk memastikan semua input valid sebelum memperbarui database.

2. Kustomisasi Desain dengan CSS/Framework CSS:
- Halaman Login dan Register: Saya mendesain ulang halaman ini untuk meningkatkan pengalaman pengguna dengan menggunakan Bootstrap. Saya memilih formulir yang lebih modern dan interaktif, serta menambahkan efek visual seperti shadow dan transition untuk membuat tampilan lebih dinamis.

- Halaman Tambah Produk: Saya menyertakan elemen form yang diperlukan dan menggunakan Tailwind CSS untuk styling. Setiap elemen form didesain untuk konsisten dan responsif, memastikan bahwa halaman ini dapat diakses dengan baik di berbagai perangkat.

3. Desain Halaman Daftar Produk: Untuk kasus ketika belum ada produk yang tersimpan, saya menyiapkan sebuah layout yang menampilkan gambar dan pesan yang estetik menggunakan CSS. Gambar dan teks tersebut memberitahu pengguna bahwa belum ada produk yang tersimpan.
Saat produk sudah tersimpan, saya menggunakan card untuk menampilkan produk. Saya memastikan bahwa setiap card dirancang untuk menonjolkan informasi penting dan menyediakan dua tombol fungsi—edit dan hapus—yang memudahkan pengelolaan produk.

4. Pembuatan Navbar yang Responsif: Saya merancang navbar yang responsif menggunakan Flexbox dan media queries untuk memastikan bahwa navigasi tetap fungsional dan estetik di berbagai ukuran layar. Navbar ini termasuk link ke halaman utama aplikasi seperti Beranda, Tentang, Daftar Produk, Registrasi, dan Login.