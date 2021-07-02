# Image Compression with SVD
**Revisi *26 Juli 2021***

Tugas CaIRK 2019

Memanfaatkan algoritma Singular Value Decomposition untuk kompresi gambar

## General Description
Algoritma SVD merupakan salah satu metode dalam aljabar linier untuk memfaktorisasi suatu matriks A berukuran mxn menjadi tiga buah matriks: matriks ortogonal U dan V, serta matriks diagonal S sesuai persamaan berikut.

<div align="center">

![a=usv](https://latex.codecogs.com/png.latex?%5Cdpi%7B120%7D%20%5CLARGE%20A_%7Bm%5Ctimes%20n%7D%20%3D%20U_%7Bm%5Ctimes%20m%7D%5C%20S_%7Bm%20%5Ctimes%20n%7D%5C%20V_%7Bnxn%7D%5E%7BT%7D)

</div>

Keterangan tambahan: Matriks **U** dan **V** terdiri atas eigenvector matriks dari **A<sup>T</sup>A** dan **AA<sup>T</sup>** berurutan. Diagonal pada matriks **S** terdiri atas akar dari eigenvalue matriks **A<sup>T</sup>A** atau **AA<sup>T</sup>** (kedua matriks ini memiliki eigenvalue yang sama)

Algoritma ini sangats sering digunakan dalam bidang *data science* dan pengolahan citra. Melalui tugas ini, kamu dapat mengetahui bagaimana algoritma SVD dimanfaatkan untuk melakukan *image compression*.

Melalui ketiga matriks hasil SVD, kamu dapat melakukan aproksimasi suatu gambar yang mampu memakan ukuran lebih sedikit dari file gambar original. Metode aproksimasi ini diserahkan kepada kamu untuk diteliti lebih lanjut.

## Cara Menggunaka \

1. Cara penggunaan program
2. Penjelasan singkat tentang algoritma SVD, minimal memuat:
    - Penjelasan tentang matriks U, S, V
    - Pemanfaatan *rank* dalam kualitas kompresi gambar
3. Referensi, framework, dan library yang membantu Anda dalam mengerjakan tugas ini beserta alasan penggunaannya.

## Spesifikasi (1500 poin)
### Spesifikasi program (1300 poin):

1. Program dijalankan di console (command prompt/ terminal) biasa.
2. Program menerima input berupa path file gambar yang dikompresi (jpg atau png), serta tingkat kompresi gambar yang diinginkan (dibebaskan ke kamu format opsinya). Kamu dapat memakai gambar ini untuk uji coba program (folder in).
<div align="center">

![momo.jpg](./in/momo.jpg)
<br>

**Fig 1.** Momo
</div>

3. Program dapat dikembangkan dengan bahasa apapun (sangat disarankan menggunakan Python).
4. Penggunaan library diperbolehkan untuk pengolahan citra dan pengolahan matriks (misal: scipy, opencv2, etc), namun implementasi algoritma from scratch akan sangat dihargai. 
<br/> Namun, penggunaan library yang melakukan kompresi gambar secara langsung <b>tidak diperbolehkan</b>. (Revisi: penggunaan library untuk dekomposisi SVD diperbolehkan)
5. Program dapat menyimpan gambar hasil kompresi pada direktori default (folder out).
6. Program dapat menampilkan runtime program dan persentase ukuran memori gambar yang dikompresi terhadap gambar original. 
Gambar hasil kompresi harus memiliki kualitas dan ukuran memori yang berbeda dari gambar masukan. Dimensi gambar tetap dipertahankan.
7. **Tambahan: Gambar hasil kompresi diperbolehkan dalam mode *grayscale*.**

### Lain-lain (200 poin)
Tulis ulang README ini dengan informasi sebagai berikut

1. Cara penggunaan program
2. Penjelasan singkat tentang algoritma SVD, minimal memuat:
    - Penjelasan tentang matriks U, S, V
    - Pemanfaatan *rank* dalam kualitas kompresi gambar
3. Referensi, framework, dan library yang membantu Anda dalam mengerjakan tugas ini beserta alasan penggunaannya.

Untuk demo, kamu dapat membuat video screen record sederhana dengan *voiceover* menjelaskan implementasi algoritma pada program dan cara penggunaan program. Sekalian jelasin ini dong hehe:

1. Matkul IRK fav
2. Pengen jadi asisten matkul apa aja kalau jadi asisten (amin)
3. Ekspektasi pas udah jadi asisten IRK  

Video diupload ke GDrive atau YouTube (salah satu aja bebas). Kreativitas video tidak dinilai, jadi buat yang simpel saja ya.

## Bonus (1300 poin)
### Huffman Coding (700 poin)
Tambahkan opsi algoritma Huffman untuk melakukan kompresi gambar. Untuk bonus ini, kamu perlu menambah opsi algoritma kompresi pada program kamu. Kamu tidak perlu menentukan berapa tingkat kompresi yang diinginkan untuk kompresi dengan Huffman.

### SVD Computation (500 poin)
Dekomposisi matriks secara SVD dilakukan dengan algoritma hasil implementasi sendiri.

### RGB Compression (100 poin)
Gambar hasil kompresi yang dihasilkan tetap dalam mode warna (RGB).

***Note**: bonus hanya akan dinilai jika seluruh spek dasar berhasil diimplementasikan*

## Pengerjaan

- Buat repositori baru (*private*) lalu invite akun GitHub **williammfu**
- Pengumpulan dapat dilakukan dengan mengirimkan link repositori GitHub dan link video (GDrive atau YouTube) via email ke 13518055@std.stei.itb.ac.id
- Bila ada pertanyaan, silahkan buat *issue* baru di repositori ini

## Referensi
* https://davetang.org/file/Singular_Value_Decomposition_Tutorial.pdf

* https://www.d.umn.edu/~mhampton/m4326svd_example.pdf

* http://www.math.utah.edu/~goller/F15_M2270/BradyMathews_SVDImage.pdf