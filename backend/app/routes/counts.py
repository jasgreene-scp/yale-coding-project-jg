from fastapi import APIRouter, Query, HTTPException
from app.utils.query_loader import load_query
from app.utils.duckdb_con import get_connection

router = APIRouter()

@router.get("/")
def disease_counts(disease: str):
    try:
        con = get_connection()
        query_template = load_query("count_by_disease.sql")
        query = query_template.replace("{{DISEASE_NAME}}", disease)
        rows = con.execute(query).fetchall()
        return {row[0]: row[1] for row in rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running query: {str(e)}")
