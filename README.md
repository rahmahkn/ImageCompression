# Image Compression with SVD

Tugas CaIRK 2019

Memanfaatkan algoritma Singular Value Decomposition untuk kompresi gambar

## General Description
Algoritma SVD merupakan salah satu metode dalam aljabar linier untuk memfaktorisasi suatu matriks A berukuran mxn menjadi tiga buah matriks: matriks ortogonal U dan V, serta matriks diagonal S sesuai persamaan berikut.

<div align="center">

![a=usv](https://latex.codecogs.com/png.latex?%5Cdpi%7B120%7D%20%5CLARGE%20A_%7Bm%5Ctimes%20n%7D%20%3D%20U_%7Bm%5Ctimes%20m%7D%5C%20S_%7Bm%20%5Ctimes%20n%7D%5C%20V_%7Bnxn%7D%5E%7BT%7D)

</div>

Algoritma SVD ini sangats sering digunakan dalam bidang *data science* dan pengolahan citra. Melalui tugas ini, kita dapat mengetahui bagaimana algoritma SVD dimanfaatkan untuk melakukan *image compression*. Dari ketiga matriks hasil SVD, kita dapat melakukan aproksimasi suatu gambar yang mampu memakan ukuran lebih sedikit dari file gambar original.

### Matrix U, S, dan V
Matriks **U** dan **V** terdiri atas eigenvector matriks dari **A<sup>T</sup>A** dan **AA<sup>T</sup>** berurutan. Diagonal pada matriks **S** terdiri atas akar dari eigenvalue matriks **A<sup>T</sup>A** atau **AA<sup>T</sup>** (kedua matriks ini memiliki eigenvalue yang sama)

### Pemanfaatan Rank dalam Kualitas Kompresi Gambar
Rank dapat digunakan untuk menentukan kualitas kompresi gambar. Algoritma SVD yang melakukan aproksimasi berdasarkan matrix yang telah direduksi menjadi low-rank matrix dengan rank yang digunakan adalah rank terkecil yang paling bisa memberikan hasil terbaik untuk kompresi gambar.

## Cara Menggunakan Program
1. Masuk ke folder `src`
2. Jalankan `python main.py`
3. Pilih nomor menu yang diinginkan
4. Masukkan path dari file secara lengkap. Contoh: `D:\chair.jpg`
5. Jika memilih kompresi menggunakan SVD, pilih tingkat kompresi sesuai dengan rentang yang diberikan
6. Image yang dikompresi akan disimpan pada folder `out` dengan format nama `namafile_algoritma`

## Teknologi
Bahasa:
* Python3

Library yang digunakan:
* PIL, imageio, numpy, scipy

## Referensi
1. https://www.frankcleary.com/svdimage/
2. https://github.com/JoshuaEbenezer/huffman_encoding
3. https://github.com/williammfu/svd-image-compression
4. http://www.acme.byu.edu/wp-content/uploads/2017/08/SVD_ImageCompression.pdf
5. https://cmdlinetips.com/2020/01/image-reconstruction-using-singular-value-decomposition-svd-in-python/