# routes/health.py
from fastapi import APIRouter
from app.utils.duckdb_con import get_connection

router = APIRouter()

@router.get("/health")
def health_check():
    try:
        con = get_connection()
        con.execute("SELECT 1")
        return {"duckdb": "ok"}
    except Exception as e:
        return {"duckdb": "unavailable", "error": str(e)}