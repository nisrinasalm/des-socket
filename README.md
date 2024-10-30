# Data Encryption Standard Implementation with Socket Client-Server

| Nama | NRP | Kelas | Pembagian Kerja |
| --- | --- | ----------|--------------|
| Aulia Putri Salsabila | 5025221281 | Keamanan Informasi (B) | Server |
| Nisrina Salma Robbani | 5025221290 | Keamanan Informasi (B) | Client |

### SERVER
Kode di sisi socket server bertujuan untuk menerima koneksi dari client, kemudian bertukar pesan terenkripsi menggunakan algoritma DES (Data Encryption Standard). Server pertama-tama membuat socket, mengikatnya ke hostname dan port yang ditentukan, lalu mendengarkan koneksi masuk. Setelah client terhubung, server menerima message terenkripsi dari client, mendekripsinya menggunakan kunci dan round keys yang dihasilkan oleh DES, kemudian menampilkan message asli. Server juga dapat mengirim balasan ke client; message balasan ini dienkripsi terlebih dahulu sebelum dikirim melalui koneksi.

### DES (Data Encryption Standard)
Kode DES disini merupakan bagian dari algoritma enkripsi dan dekripsi DES (Data Encryption Standard), yang menggunakan tabel permutasi (initial dan final permutation) serta tabel substitusi (S-box) untuk mengubah data plaintext menjadi ciphertext, dan sebaliknya. Algoritma ini menerima input ASCII yang diubah ke format heksadesimal (heksa) untuk mempermudah manipulasi bit. Dengan menggunakan permutasi dan substitusi yang kompleks, DES mampu mengacak data secara efektif. Meskipun DES awalnya dirancang untuk input 64-bit, algoritma ini dapat mengelola data lebih besar dari 64-bit dengan cara memprosesnya dalam blok-blok terpisah, lalu menggabungkan hasilnya. Untuk pengujiannya program bisa diinputkan teks yang panjangnya lebih dari 8 karakter.

![image](https://github.com/user-attachments/assets/f802c814-8ee4-421b-be4e-c4ce1ab62f47)

##### Contoh 1
"Hello, this is a test message!". Teks ini memiliki 29 karakter, atau sekitar 232 bit (29 bytes).
##### Contoh 2
"Keamanan Informasi". Teks ini memiliki 18 karakter, atau sekitar 144 bit (18 bytes).


### CLIENT
Kode di sisi client bertujuan untuk mendengarkan koneksi di alamat localhost dan port 5000. Server menggunakan algoritma DES untuk enkripsi dan dekripsi pesan yang dikirim antara server dan klien. Setelah koneksi dari klien diterima, server menunggu untuk menerima pesan terenkripsi dari klien, yang kemudian didekripsi menggunakan kunci DES yang dihasilkan dari generate_keys. Pesan yang didekripsi ditampilkan, lalu server meminta input dari pengguna untuk mengirimkan balasan ke klien. Pesan balasan tersebut dienkripsi dengan kunci yang sama sebelum dikirimkan kembali ke klien. Proses ini berlanjut hingga tidak ada lagi data yang diterima dari klien. Kunci yang digunakan dalam kode ini ditetapkan secara _hardcode_ yang diibaratkan seperti situasi di mana dua pihak (server dan client) sudah mengetahui key yang sama.
