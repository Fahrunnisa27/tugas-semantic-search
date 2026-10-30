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

**Penjelasan dengan bahasa sendiri:** [ISI setelah memahami dan mencoba alur indexing dan search]

## Embedding Model
**Model:** `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.

**Apa fungsi embedding model?** [ISI SENDIRI setelah menguji]

## Vector Database
**Apa fungsi Qdrant?** [ISI SENDIRI]

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
**Query:** minuman dingin dari buah yang segar  
**Top Result:** [ISI OUTPUT ASLI]  
**Similarity Score:** [ISI OUTPUT ASLI]  
**Apakah relevan? Kenapa?** [ISI SENDIRI]

### Query 2
**Query:** makanan berkuah hangat yang ada bola dagingnya  
**Top Result:** [ISI OUTPUT ASLI]  
**Similarity Score:** [ISI OUTPUT ASLI]  
**Apakah relevan? Kenapa?** [ISI SENDIRI]

### Query 3
**Query:** camilan manis yang dibuat dari buah digoreng  
**Top Result:** [ISI OUTPUT ASLI]  
**Similarity Score:** [ISI OUTPUT ASLI]  
**Apakah relevan? Kenapa?** [ISI SENDIRI]

### Query 4
**Query:** nasi dengan rasa gurih dan lauk untuk sarapan  
**Top Result:** [ISI OUTPUT ASLI]  
**Similarity Score:** [ISI OUTPUT ASLI]  
**Apakah relevan? Kenapa?** [ISI SENDIRI]

### Query 5
**Query:** minuman hangat dari rempah untuk cuaca dingin  
**Top Result:** [ISI OUTPUT ASLI]  
**Similarity Score:** [ISI OUTPUT ASLI]  
**Apakah relevan? Kenapa?** [ISI SENDIRI]

## Experiment 2 - Top-K
**Query yang sama:** makanan berkuah hangat yang ada bola dagingnya

### Top-K = 1
**Actual Result:** [ISI HASIL ASLI]

### Top-K = 3
**Actual Result:** [ISI HASIL ASLI]

### Top-K = 5
**Actual Result:** [ISI HASIL ASLI]

**Apa yang berubah ketika Top-K diperbesar?** [ISI SESUAI HASIL]

**Apakah menambah Top-K selalu membuat hasil lebih baik?** [ISI PENDAPAT BERDASARKAN TES]

## Experiment 3 - Bad Retrieval
**Query:** [ISI QUERY YANG MEMANG MENGHASILKAN HASIL ANEH]

**Actual Results:** [ISI HASIL ASLI]

**Similarity Score:** [ISI HASIL ASLI]

**Kenapa kurang relevan?** [ISI SENDIRI]

**Apa penyebabnya menurut kalian?** [ISI SENDIRI]

## Personal Reflection
1. **Sebelum tugas ini, bagaimana membayangkan search engine bekerja, dan apa yang berubah?** [ISI SENDIRI]
2. **Perbedaan terbesar keyword search dan semantic search?** [ISI SENDIRI]
3. **Fungsi embedding dalam semantic search?** [ISI SENDIRI]
4. **Mengapa embedding tidak cukup disimpan dalam list Python untuk data sangat banyak?** [ISI SENDIRI]
5. **Bagian project paling sulit dipahami?** [ISI SENDIRI]
6. **Bagian kode paling banyak dibantu AI?** [ISI SENDIRI secara jujur]
7. **Jelaskan bagaimana bagian kode itu bekerja dengan bahasa sendiri.** [ISI SENDIRI]
8. **Project bisa dikembangkan jadi aplikasi apa?** [ISI SENDIRI]

## AI Usage
**AI tools yang digunakan:** [ISI SESUAI YANG BENAR-BENAR DIGUNAKAN]

**AI membantu bagian apa?** [ISI JUJUR; contoh: struktur awal project dan penjelasan error]

**Apa yang saya tentukan/perbaiki/ubah sendiri?** [ISI BERDASARKAN PROSES NYATA]

## Pengumpulan
Upload source code dan README yang sudah lengkap ke repo GitHub `tugas-semantic-search`. Pastikan `qdrant_data/` dan `venv/` tidak di-push. Kumpulkan **link repository** ke LMS, bukan ZIP.
