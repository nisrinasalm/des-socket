# Data Encryption Standard Implementation with Socket Client-Server

| Nama | NRP | Kelas | Pembagian Kerja |
| --- | --- | ----------|--------------|
| Aulia Putri Salsabila | 5025221281 | Keamanan Informasi (B) | Server |
| Nisrina Salma Robbani | 5025221290 | Keamanan Informasi (B) | Client |

### SERVER
Kode di sisi socket server bertujuan untuk menerima koneksi dari client, kemudian bertukar pesan terenkripsi menggunakan algoritma DES (Data Encryption Standard). Server pertama-tama membuat socket, mengikatnya ke hostname dan port yang ditentukan, lalu mendengarkan koneksi masuk. Setelah client terhubung, server menerima message terenkripsi dari client, mendekripsinya menggunakan kunci dan round keys yang dihasilkan oleh DES, kemudian menampilkan message asli. Server juga dapat mengirim balasan ke client; message balasan ini dienkripsi terlebih dahulu sebelum dikirim melalui koneksi.

### DES (Data Encryption Standard
Algoritma DES merupakan metode enkripsi simetris dengan berbagai table dan function yang digunakan untuk mengatur ulang dan memodifikasi blok data selama proses enkripsi. Fungsi ascii2hex digunakan untuk mengonversi string ASCII ke format hexadecimal. Fungsi hex2bin() mengonversi data heksadesimal ke biner untuk memudahkan transformasi bit-by-bit pada data yang dienkripsi, di mana setiap langkah bertujuan untuk menciptakan data yang aman dengan permutasi dan substitusi berulang.
