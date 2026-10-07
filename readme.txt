================================================================================
KRIPTOGRAFI M2 - CIPHER ENGINE
Dokumentasi Proyek dan Panduan Penggunaan
================================================================================

1. DESKRIPSI PROYEK
Proyek ini merupakan aplikasi kriptografi klasik yang mengimplementasikan empat
metode cipher:
- Beaufort Cipher
- Caesar Cipher
- Four-Square Cipher
- Vigenere Cipher

Aplikasi menyediakan dua cara pengoperasian:
1. Antarmuka Web (GUI) berbasis Flask yang ramah pengguna.
2. Antarmuka Baris Perintah (CLI / Terminal) untuk setiap modul cipher.


2. STRUKTUR DIREKTORI
KriptografiM2_KID/
│
├── main.py              : Server aplikasi web berbasis Flask
├── Beaufort.py          : Algoritma dan CLI untuk Beaufort Cipher
├── Caesar Cipher.py     : Algoritma dan CLI untuk Caesar Cipher
├── Four Square.py       : Algoritma dan CLI untuk Four-Square Cipher
├── Vigenere.py          : Algoritma untuk Vigenere Cipher
├── templates/
│   └── index.html       : Tampilan antarmuka web (UI)
├── design(m2).md        : Dokumentasi token dan desain antarmuka
└── readme.txt           : Petunjuk instalasi dan panduan penggunaan


3. PERSYARATAN SISTEM
- Python 3.8 atau versi yang lebih baru.
- Library Flask (diperlukan untuk menjalankan antarmuka web).
  Catatan: Menjalankan skrip CLI secara mandiri hanya memerlukan pustaka standar
  Python (tanpa instalasi paket tambahan).


4. INSTALASI DEPENDENSI
Buka terminal (Command Prompt / PowerShell / Terminal) di folder proyek ini,
lalu jalankan:

    pip install flask


5. PANDUAN PENGGUNAAN

A. MENJALANKAN APLIKASI WEB
1. Jalankan perintah berikut di terminal:
    python main.py

2. Aplikasi akan memulai server lokal dan secara otomatis membuka browser
   ke alamat:
    http://127.0.0.1:5000

3. Langkah-langkah penggunaan pada antarmuka web:
   a. Pilih metode cipher yang ingin digunakan pada bagian atas:
      - Beaufort
      - Caesar
      - Four-Square
      - Vigenere
   b. Tentukan jenis aksi: "ENKRIPSI" atau "DEKRIPSI".
   c. Masukkan teks input:
      - Ketik atau tempel teks pada kotak input teks, ATAU
      - Pilih tab "Upload File .txt" lalu unggah file teks yang ingin diproses.
   d. Masukkan kunci sesuai metode cipher yang dipilih:
      - Beaufort Cipher : Masukkan kata kunci teks (huruf A-Z) atau unggah
                          file teks kunci.
      - Caesar Cipher   : Tentukan nilai pergeseran (shift) berupa angka 0-25.
      - Four-Square     : Masukkan dua kata kunci terpisah (Key 1 dan Key 2).
      - Vigenere Cipher : Masukkan kata kunci teks (huruf A-Z) atau unggah
                          file teks kunci.
   e. Klik tombol "PROSES SEKARANG".
   f. Hasil akan langsung muncul pada kotak "Hasil Output".
   g. Anda dapat menyalin hasil ke clipboard atau mengunduhnya sebagai file
      "output.txt" dengan tombol "Download .txt".


B. MENJALANKAN MODUL STANDALONE MELALUI TERMINAL (CLI)
Setiap algoritma cipher dapat dijalankan langsung di terminal:

1. Beaufort Cipher
   Perintah:
    python Beaufort.py
   Fitur Menu:
    - 1: Enkripsi teks manual melalui terminal
    - 2: Dekripsi teks manual melalui terminal
    - 3: Enkripsi file input .txt dan simpan ke file output .txt
    - 4: Dekripsi file input .txt dan simpan ke file output .txt
    - 5: Keluar

2. Caesar Cipher
   Perintah:
    python "Caesar Cipher.py"
   Fitur Menu:
    - 1: Enkripsi teks manual (input teks dan nilai shift 0-25)
    - 2: Dekripsi teks manual
    - 3: Enkripsi file input .txt dan simpan ke file output .txt
    - 4: Dekripsi file input .txt dan simpan ke file output .txt
    - 5: Keluar

3. Four-Square Cipher
   Perintah:
    python "Four Square.py"
   Fitur Menu:
    - 1: Enkripsi teks manual (input teks, Key 1, dan Key 2)
    - 2: Dekripsi teks manual
    - 3: Enkripsi file input .txt dan simpan ke file output .txt
    - 4: Dekripsi file input .txt dan simpan ke file output .txt
    - 5: Keluar

4. Vigenere Cipher
   Perintah:
    python Vigenere.py
   Skrip akan menjalankan pengujian contoh enkripsi dan dekripsi otomatis.


6. DETAIL ALGORITMA CIPHER
- Beaufort Cipher:
  Cipher substitusi polialfabetik yang bersifat simetris (enkripsi dan dekripsi
  menggunakan formula perhitungan yang sama):
  C = (Key - Plaintext) mod 26
  Karakter diproses dalam format huruf kapital A-Z.

- Caesar Cipher:
  Cipher substitusi monoalfabetik dengan menggeser urutan alfabet:
  Enkripsi: C = (Plaintext + Key) mod 26
  Dekripsi: P = (Ciphertext - Key) mod 26
  Mempertahankan huruf besar, huruf kecil, serta karakter non-alfabet.

- Four-Square Cipher:
  Cipher substitusi poligrafik yang memproses huruf secara berpasangan (digram)
  menggunakan empat bujur sangkar 5x5:
  Alfabet 25 huruf (huruf 'J' digabung ke 'I'). Jika panjang teks ganjil, huruf
  'X' akan ditambahkan di akhir teks.

- Vigenere Cipher:
  Cipher substitusi polialfabetik menggunakan kata kunci berulang:
  Enkripsi: C = (Plaintext + Key) mod 26
  Dekripsi: P = (Ciphertext - Key + 26) mod 26
  Mempertahankan format huruf besar dan huruf kecil.


7. TIPS & CATATAN TAMBAHAN
- Pastikan file teks yang diunggah menggunakan encoding UTF-8 standar.
- Untuk menghentikan server web di terminal, tekan Ctrl + C.
================================================================================
