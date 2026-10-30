"""Semantic Search sederhana: SentenceTransformers + Qdrant lokal + FastAPI."""

from functools import lru_cache
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

from data import documents

app = FastAPI(title="Semantic Search Makanan & Minuman", version="1.0.0")
MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
COLLECTION = "menu_makanan_minuman"
DATABASE_PATH = str(Path(__file__).resolve().parent / "qdrant_data")


class SearchRequest(BaseModel):
    query: str = Field(min_length=2, description="Kalimat yang ingin dicari berdasarkan makna")
    top_k: int = Field(default=3, ge=1, le=30)


class SearchResult(BaseModel):
    text: str
    category: str
    score: float


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]


@lru_cache(maxsize=1)
def get_model() -> SentenceTransformer:
    # Pada penggunaan pertama model akan diunduh (butuh internet).
    return SentenceTransformer(MODEL_NAME)


@lru_cache(maxsize=1)
def get_db() -> QdrantClient:
    # Qdrant local persistent: tidak perlu Docker atau akun cloud.
    return QdrantClient(path=DATABASE_PATH)


@app.get("/health")
def health():
    return {"status": "OK", "total_dataset": len(documents), "collection": COLLECTION}


@app.post("/index")
def index_dataset():
    """Ubah 30 kalimat menjadi vektor lalu simpan bersama payload."""
    try:
        model = get_model()
        db = get_db()
        texts = [item["text"] for item in documents]
        embeddings = model.encode(texts, show_progress_bar=False).tolist()
        dimension = len(embeddings[0])

        # Reset collection agar setiap indexing tidak menggandakan data.
        if db.collection_exists(COLLECTION):
            db.delete_collection(COLLECTION)
        db.create_collection(
            collection_name=COLLECTION,
            vectors_config=models.VectorParams(size=dimension, distance=models.Distance.COSINE),
        )
        points = [
            models.PointStruct(id=i + 1, vector=vector, payload=item)
            for i, (vector, item) in enumerate(zip(embeddings, documents))
        ]
        db.upsert(collection_name=COLLECTION, points=points, wait=True)
        return {"message": "Indexing berhasil", "jumlah_data": len(points), "vector_size": dimension}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Indexing gagal: {exc}") from exc


@app.post("/search", response_model=SearchResponse)
def semantic_search(request: SearchRequest):
    """Cari dokumen terdekat memakai cosine similarity di Qdrant."""
    try:
        db = get_db()
        if not db.collection_exists(COLLECTION):
            raise HTTPException(status_code=400, detail="Dataset belum di-index. Jalankan POST /index dahulu.")
        query_vector = get_model().encode(request.query).tolist()
        found = db.query_points(
            collection_name=COLLECTION,
            query=query_vector,
            limit=request.top_k,
            with_payload=True,
        ).points
        return SearchResponse(
            query=request.query,
            results=[
                SearchResult(
                    text=point.payload.get("text", ""),
                    category=point.payload.get("category", ""),
                    score=round(float(point.score), 4),
                )
                for point in found
            ],
        )
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Pencarian gagal: {exc}") from exc
