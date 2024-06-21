# ForwadingMessageBot
Bot telegram untuk memforward pesan dari bot tertentu, atau dari channel, dari grup, dari orang ke grup kita. 

Berguna untuk memforwading pesan dari GRUP/BOT/CHANNEL atau Private CHAT ke GRUP lain dengan catatan forwarding message tidak di batasi. 
Install Python versi 3.12.3 ( versi lain mungkin gak kompatibel dengan defency ).

Cara Run di windows...
1. Buka terminal CMD manapun, navigasi ke folder kerja kalian atau :
2. Buka Windows Explore buat folder baru, nanti pada address bard ketikan cmd CONTOH
3. ```cmd C:\Users\user\Downloads\Pelanggan\SAGITA FEBRIYANTI```
4. Habis itu jalankan perintah ini, satu perintah satu kali klik enter tunggu sampai proses selesai baru jalankan perintah lain hingga semua perintah di eksekusi.


```git clone https://github.com/NetzkuOfficial/ForwadingMessageBot.git```

Setelah di clone masuk ke folder kerja ketik perintah 


```cd ForwadingMessageBot```

Setelah masuk ke folder kerja, kita buat terlebih dahulu lingkungan VIRTUAL ( biar gak konflik dengan program lain )
Jalankan perintah berikut ( Untuk sistem operasi windows )

Untuk pertama kali saja, install pustaka pembuatan virtualenv di python publik.

```pip install virtualenv```

Settelah itu baru jalankan perintah pembuatan env di terminal berikut ini 

```python -m venv folder-saya```

Jalankan/enter, setelah itu jalankan perintah berikut ini : 

```folder-saya\Scripts\activate```




lalu install semua defency dalam file requirements.txt, jalankan printah berikut

```pip install -r requirements.txt```

Buka teks editor kesayangan kamu vscode, sublimetext, notepad. Lalu buat file baru isi teks berikut ini : 
```
API_ID=API_ID_ANDA
API_HASH=API_HASH_ANDA
PHONE_NUMBER=+62xxxx #(NO TELEGRAM ANDA )
SENDER_ID=ID_SENDER #( YANG PESAN NYA MAU DI FORWARD )
GRUP_ID=ID_GRUP #(ID TEMPAT GRUP MENAMPUNG )
```
Simpan dengan nama file .env

Buat yang bingung di mana mendapatkan API_ID, API_HASH : login di https://my.telegram.org dengan account anda, buat akun development baru pilih versi web lalu nanti akan jadi deh.
Buat yang bingung dapatin id grup : Chat ke https://t.me/NetzkuBot tambahkan ke grup anda ( super grup/group ) lalu kirim pesan /id 

Perintah terakhir menjalankan BOT, ketik perintah di terminal lalu enter.

```python main.py```


Untuk memodifikasi script ini silakan lakukan GARPU ke repositori pribadi kamu, lalu edit di sana. Apabila ada pertanyaan contact saya di https://t.me/ryanx bot ini hanya untuk iseng-iseng, source code merupakan sumber kode mentah yang tidak mengandung banyak program ataupun code.
