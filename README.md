# Semantic Search & Vector Database

## Project Information
**Nama Project:** Semantic Search Makanan & Minuman  
**Tema Dataset:** Makanan dan minuman Indonesia  
**Deskripsi Singkat:** API untuk mencari makanan atau minuman berdasarkan kemiripan makna kalimat, bukan hanya kata yang sama.

## Dataset
**Jumlah Data:** 30 data.  
**Kategori yang Digunakan:** `makanan_berat` (10), `camilan` (10), `minuman` (10).  
**Kenapa memilih dataset tersebut?** Saya memilih tema makanan dan minuman karena dekat dengan kehidupan sehari-hari dan mudah diuji menggunakan kalimat pencarian yang natural.

## Tech Stack
Python, FastAPI, Pydantic, SentenceTransformers (`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`), Qdrant lokal.

## Cara Menjalankan
1. `python -m venv venv`
2. Windows CMD: `venv\Scripts\activate.bat`
3. `python -m pip install -r requirements.txt`
4. `fastapi dev main.py`
5. Buka `http://127.0.0.1:8000/docs`.
6. Jalankan `POST /index` **satu kali dahulu**, lalu `POST /search`.

**Catatan:** Saat digunakan pertama kali, model SentenceTransformers akan diunduh dari internet. Ukurannya cukup besar sehingga proses awal bisa lebih lama. Qdrant berjalan lokal melalui folder `qdrant_data/`, tidak perlu Docker. Folder ini tidak di-upload ke GitHub. Jika project dipindahkan, jalankan `/index` kembali.

## Application Flow
Dataset → Embedding Model → Vector → Qdrant.  
Query pengguna → Embedding Model → Query Vector → Qdrant Search → Top-K Results.

**Penjelasan dengan bahasa sendiri:** Cara kerja aplikasi ini dimulai dari dataset makanan dan minuman yang diubah menjadi vector menggunakan embedding model, lalu disimpan ke Qdrant. Setelah itu, ketika pengguna memasukkan kalimat pencarian, aplikasi akan mengubah kalimat tersebut menjadi vector juga. Kemudian Qdrant mencari data yang maknanya paling mirip dan menampilkan beberapa hasil sesuai nilai Top-K beserta similarity score-nya.

## Embedding Model
**Model:** `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.

**Apa fungsi embedding model?** 
Menurut saya, embedding model berfungsi untuk mengubah teks menjadi bentuk angka atau vector agar bisa dibandingkan dengan data lainnya. Jadi, aplikasi tidak hanya mencari kata yang sama, tetapi juga bisa mencari berdasarkan kemiripan makna dari kalimat yang dimasukkan pengguna.

## Vector Database
**Apa fungsi Qdrant?** 
Qdrant digunakan untuk menyimpan vector dari dataset makanan dan minuman, lalu mencari data yang paling mirip dengan pencarian pengguna. Selain vector, Qdrant juga menyimpan informasi seperti teks dan kategori makanan atau minuman. Jadi, hasil pencariannya bisa menampilkan deskripsi, kategori, dan similarity score.

**Apa yang disimpan di payload?** `text` dan `category`.

## API Endpoint
- `GET /health`: cek server dan jumlah dataset.
- `POST /index`: ubah dataset menjadi embedding dan simpan ke Qdrant.
- `POST /search`: cari teks yang maknanya mirip dan tampilkan skor.

## Example Request
```json
{
  "query": "minuman dingin dari buah yang segar",
  "top_k": 3
}
```

## Example Response
[PASTE **actual response** dari Swagger `/search`, jangan isi dengan respons buatan]

## Experiment 1 - Semantic Search
Gunakan 5 query **yang berbeda dari bunyi dataset**, lalu isi dengan hasil asli aplikasi.

### Query 1
Aku ingin minuman hangat yang terbuat dari rempah-rempah.  
**Top Result:** {
  "query": "aku ingin minuman hangat yang terbuat dari rempah-rempah",
  "results": [
    {
      "text": "Wedang jahe adalah minuman hangat berbahan jahe dan gula yang terasa pedas ringan.",
      "category": "minuman",
      "score": 0.7036
    },
    {
      "text": "Cokelat panas adalah minuman hangat dari bubuk cokelat dan susu.",
      "category": "minuman",
      "score": 0.6966
    },
    {
      "text": "Lemon tea adalah teh dengan rasa lemon yang biasa disajikan segar dan dingin.",
      "category": "minuman",
      "score": 0.6141
    }
  ]  

**Apakah relevan? Kenapa?** Menurut saya, hasilnya relevan jika minuman yang ditemukan memang sesuai dengan pencarian minuman hangat berbahan rempah.

### Query 2
aku lagi lapar dan ingin makanan berat dengan rasa pedas  
**Top Result:** 
{
  "query": "aku lagi lapar dan ingin makanan berat dengan rasa pedas",
  "results": [
    {
      "text": "Wedang jahe adalah minuman hangat berbahan jahe dan gula yang terasa pedas ringan.",
      "category": "minuman",
      "score": 0.4848
    },
    {
      "text": "Pempek adalah olahan ikan dan tepung yang disantap dengan kuah cuko asam pedas.",
      "category": "camilan",
      "score": 0.4362
    },
    {
      "text": "Bakso adalah bola daging yang disajikan dalam kuah hangat bersama mie atau bihun.",
      "category": "makanan_berat",
      "score": 0.4273
    }
  ]
}  

**Apakah relevan? Kenapa?**
Menurut saya, hasilnya relevan kalau makanan yang muncul memang termasuk makanan berat dengan rasa pedas, sesuai dengan yang saya cari. Ini menunjukkan bahwa aplikasi bisa mencari berdasarkan kemiripan makna, bukan hanya kata yang sama.

### Query 3
aku mencari camilan manis untuk menemani waktu santai sore 
**Top Result:** 
{
  "query": "aku mencari camilan manis untuk menemani waktu santai sore",
  "results": [
    {
      "text": "Wedang jahe adalah minuman hangat berbahan jahe dan gula yang terasa pedas ringan.",
      "category": "minuman",
      "score": 0.5924
    },
    {
      "text": "Martabak manis adalah kue tebal dengan isian cokelat, keju, atau kacang.",
      "category": "camilan",
      "score": 0.4605
    },
    {
      "text": "Lemon tea adalah teh dengan rasa lemon yang biasa disajikan segar dan dingin.",
      "category": "minuman",
      "score": 0.4332
    }
  ]
}  

**Apakah relevan? Kenapa?** 
Menurut saya, hasilnya relevan jika makanan yang muncul termasuk camilan manis yang cocok dimakan saat santai. Hal ini menunjukkan bahwa aplikasi dapat memahami maksud pencarian saya meskipun kalimat yang digunakan tidak sama persis dengan data yang tersimpan.

### Query 4
minuman dingin yang menyegarkan saat cuaca panas
**Top Result:** 
{
  "query": "minuman dingin yang menyegarkan saat cuaca panas",
  "results": [
    {
      "text": "Cokelat panas adalah minuman hangat dari bubuk cokelat dan susu.",
      "category": "minuman",
      "score": 0.7761
    },
    {
      "text": "Wedang jahe adalah minuman hangat berbahan jahe dan gula yang terasa pedas ringan.",
      "category": "minuman",
      "score": 0.7715
    },
    {
      "text": "Lemon tea adalah teh dengan rasa lemon yang biasa disajikan segar dan dingin.",
      "category": "minuman",
      "score": 0.6315
    }
  ]
}


**Apakah relevan? Kenapa?** 
Menurut saya, hasilnya kurang relevan karena saya mencari minuman dingin yang menyegarkan saat cuaca panas, tetapi dua hasil teratas justru minuman hangat, yaitu cokelat panas dan wedang jahe. Hasil ketiga, yaitu lemon tea, lebih sesuai dengan pencarian saya karena bisa disajikan dingin dan menyegarkan. Jadi, meskipun similarity score dua hasil pertama cukup tinggi, belum tentu hasilnya sesuai dengan yang dicari.

### Query 5
aku ingin makanan berkuah hangat yang mengenyangkan  
**Top Result:** 
{
  "query": "aku ingin makanan berkuah hangat yang mengenyangkan",
  "results": [
    {
      "text": "Wedang jahe adalah minuman hangat berbahan jahe dan gula yang terasa pedas ringan.",
      "category": "minuman",
      "score": 0.5908
    },
    {
      "text": "Sate ayam merupakan potongan daging ayam yang ditusuk lalu dibakar dan disajikan dengan bumbu kacang.",
      "category": "makanan_berat",
      "score": 0.4961
    },
    {
      "text": "Bakso adalah bola daging yang disajikan dalam kuah hangat bersama mie atau bihun.",
      "category": "makanan_berat",
      "score": 0.4821
    }
  ]
}

**Apakah relevan? Kenapa?** 
Menurut saya, hasilnya kurang relevan karena saya mencari makanan berkuah hangat yang mengenyangkan, tetapi hasil pertama justru wedang jahe yang merupakan minuman, sedangkan hasil kedua sate ayam yang tidak berkuah. Hasil ketiga, yaitu bakso, lebih sesuai karena termasuk makanan berkuah hangat dan mengenyangkan. Jadi, aplikasi masih belum sepenuhnya memahami maksud pencarian meskipun sudah menggunakan semantic search.

## Experiment 2 - Top-K
**Query yang sama:** minuman dingin yang menyegarkan saat cuaca panas

### Top-K = 1
**Actual Result:** 
{
  "query": "minuman dingin yang menyegarkan saat cuaca panas",
  "results": [
    {
      "text": "Cokelat panas adalah minuman hangat dari bubuk cokelat dan susu.",
      "category": "minuman",
      "score": 0.7761
    }
  ]
}

### Top-K = 3
**Actual Result:** 
{
  "query": "minuman dingin yang menyegarkan saat cuaca panas",
  "results": [
    {
      "text": "Cokelat panas adalah minuman hangat dari bubuk cokelat dan susu.",
      "category": "minuman",
      "score": 0.7761
    },
    {
      "text": "Wedang jahe adalah minuman hangat berbahan jahe dan gula yang terasa pedas ringan.",
      "category": "minuman",
      "score": 0.7715
    },
    {
      "text": "Lemon tea adalah teh dengan rasa lemon yang biasa disajikan segar dan dingin.",
      "category": "minuman",
      "score": 0.6315
    }
  ]
}

### Top-K = 5
**Actual Result:** 
{
  "query": "minuman dingin yang menyegarkan saat cuaca panas",
  "results": [
    {
      "text": "Cokelat panas adalah minuman hangat dari bubuk cokelat dan susu.",
      "category": "minuman",
      "score": 0.7761
    },
    {
      "text": "Wedang jahe adalah minuman hangat berbahan jahe dan gula yang terasa pedas ringan.",
      "category": "minuman",
      "score": 0.7715
    },
    {
      "text": "Lemon tea adalah teh dengan rasa lemon yang biasa disajikan segar dan dingin.",
      "category": "minuman",
      "score": 0.6315
    },
    {
      "text": "Matcha latte merupakan campuran bubuk teh hijau dan susu yang dapat disajikan dingin atau hangat.",
      "category": "minuman",
      "score": 0.5365
    },
    {
      "text": "Jus alpukat adalah minuman kental dari buah alpukat yang diblender bersama air atau susu.",
      "category": "minuman",
      "score": 0.5191
    }
  ]
}

**Apa yang berubah ketika Top-K diperbesar?** 
Dari hasil pengujian, semakin besar nilai Top-K, semakin banyak hasil pencarian yang ditampilkan. Saat Top-K 1, hanya muncul cokelat panas. Ketika Top-K 3, hasilnya bertambah menjadi wedang jahe dan lemon tea. Lalu saat Top-K 5, muncul lagi matcha latte dan jus alpukat. Menurut saya, dengan memperbesar Top-K, pengguna bisa melihat lebih banyak pilihan, termasuk minuman dingin yang lebih sesuai dengan pencarian.

**Apakah menambah Top-K selalu membuat hasil lebih baik?** 
Menurut saya, tidak selalu. Karena walaupun jumlah hasil bertambah, hasil paling atas tetap cokelat panas dan wedang jahe yang kurang sesuai dengan pencarian minuman dingin. Tetapi dengan Top-K yang lebih besar, saya bisa menemukan lemon tea dan matcha latte yang lebih sesuai. Jadi, Top-K membantu memberikan lebih banyak pilihan, tetapi tidak menjamin semua hasil relevan.

## Experiment 3 - Bad Retrieval
**Query:** minuman dingin yang menyegarkan saat cuaca panas

**Actual Results:**
{
  "query": "minuman dingin yang menyegarkan saat cuaca panas",
  "results": [
    {
      "text": "Cokelat panas adalah minuman hangat dari bubuk cokelat dan susu.",
      "category": "minuman",
      "score": 0.7761
    },
    {
      "text": "Wedang jahe adalah minuman hangat berbahan jahe dan gula yang terasa pedas ringan.",
      "category": "minuman",
      "score": 0.7715
    },
    {
      "text": "Lemon tea adalah teh dengan rasa lemon yang biasa disajikan segar dan dingin.",
      "category": "minuman",
      "score": 0.6315
    }
  ]
}

**Kenapa kurang relevan?** 
Menurut saya, hasilnya kurang relevan karena saya mencari minuman dingin yang menyegarkan, tetapi dua hasil teratas justru cokelat panas dan wedang jahe yang merupakan minuman hangat. Padahal lemon tea yang lebih sesuai dengan pencarian malah berada di urutan ketiga.

**Apa penyebabnya menurut kalian?** 
Menurut saya, kemungkinan model lebih menangkap kemiripan pada kata dan makna tentang minuman, tetapi kurang memperhatikan perbedaan antara dingin dan hangat. Akibatnya, minuman hangat tetap mendapatkan similarity score yang tinggi meskipun tidak sesuai dengan maksud pencarian saya.

## Personal Reflection
1. **Sebelum tugas ini, bagaimana membayangkan search engine bekerja, dan apa yang berubah?** 
Sebelumnya saya mengira search engine itu cuma mencari data berdasarkan kata yang kita ketik. Jadi kalau kata yang dicari tidak ada di data, hasilnya mungkin tidak muncul. Setelah mencoba semantic search, saya baru tahu kalau pencarian juga bisa berdasarkan kemiripan makna, walaupun kalimat yang digunakan berbeda dengan data aslinya.

2. **Perbedaan terbesar keyword search dan semantic search?**
Menurut saya, perbedaan terbesarnya ada pada cara pencariannya. Keyword search lebih fokus pada kata yang sama, sedangkan semantic search mencoba mencari data berdasarkan makna dari kalimat yang dimasukkan. Jadi, semantic search bisa menemukan hasil yang berkaitan meskipun tidak menggunakan kata yang sama persis.

3. **Fungsi embedding dalam semantic search?**
Embedding berfungsi untuk mengubah teks menjadi bentuk angka atau vector supaya bisa diproses oleh sistem. Dengan begitu, aplikasi bisa membandingkan kemiripan antara query pengguna dan data yang sudah disimpan.

4. **Mengapa embedding tidak cukup disimpan dalam list Python untuk data sangat banyak?** 
Menurut saya, kalau datanya sudah sangat banyak, menyimpan dan mencari vector hanya menggunakan list Python bisa menjadi kurang efisien. Karena itu, Qdrant digunakan untuk menyimpan dan mencari vector dengan lebih terstruktur, terutama jika jumlah data semakin besar.

5. **Bagian project paling sulit dipahami?** 
bagian yang paling sulit menurut saya adalah memahami bagaimana embedding dan Qdrant bekerja. Awalnya saya masih bingung bagaimana kalimat bisa diubah menjadi vector dan digunakan untuk mencari data yang mirip. Selain itu, saya juga sempat mengalami kendala saat menjalankan project karena terminal belum berada di folder yang benar.

6. **Bagian kode paling banyak dibantu AI?** 
Bagian yang paling banyak dibantu oleh ChatGPT adalah struktur awal project, kode untuk mengubah teks menjadi embedding, menghubungkan aplikasi ke Qdrant, dan membuat endpoint pencarian menggunakan FastAPI. Saya juga menggunakan AI untuk membantu memahami error yang muncul saat menjalankan aplikasi.

7. **Jelaskan bagaimana bagian kode itu bekerja dengan bahasa sendiri.** 
Dari yang saya pahami, awalnya aplikasi mengambil data makanan dan minuman, lalu mengubah setiap deskripsinya menjadi vector menggunakan SentenceTransformers. Setelah itu, vector disimpan ke Qdrant bersama informasi kategori dan teksnya. Ketika pengguna memasukkan pencarian, kalimat tersebut juga diubah menjadi vector, kemudian Qdrant mencari data yang paling mirip dan menampilkan hasil beserta similarity score.

8. **Project bisa dikembangkan jadi aplikasi apa?** 
Menurut saya, project ini bisa dikembangkan menjadi aplikasi rekomendasi makanan dan minuman. Jadi, pengguna cukup mengetik makanan atau minuman seperti apa yang mereka inginkan, misalnya makanan pedas atau minuman segar, lalu aplikasi memberikan beberapa rekomendasi yang sesuai. Kalau dikembangkan lagi, bisa ditambahkan filter kategori agar hasil pencariannya lebih tepat.

## AI Usage
**AI tools yang digunakan:** 
ChatGPT.

**AI membantu bagian apa?**
Saya menggunakan ChatGPT untuk membantu membuat struktur awal project dan beberapa bagian kode Python, FastAPI, SentenceTransformers, serta Qdrant. Selain itu, AI juga membantu menjelaskan cara menjalankan aplikasi, mengatasi error, dan memahami hasil pengujian semantic search.

**Apa yang saya tentukan/perbaiki/ubah sendiri?** 
Saya memilih menggunakan dataset makanan dan minuman karena menurut saya topiknya mudah dipahami dan bisa dicoba dengan berbagai kalimat pencarian. Saya juga menjalankan aplikasi sendiri melalui Swagger UI dan mencoba lima query berbeda, serta membandingkan hasil Top-K 1, 3, dan 5. Dari pengujian tersebut, saya menemukan bahwa hasil pencarian belum selalu sesuai, contohnya saat mencari minuman dingin tetapi hasil teratas justru cokelat panas dan wedang jahe. Dari situ saya belajar bahwa similarity score yang tinggi belum tentu berarti hasilnya paling relevan.

