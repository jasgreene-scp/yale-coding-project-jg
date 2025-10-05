from fastapi import APIRouter, HTTPException
from app.utils.query_loader import load_query
from app.utils.duckdb_con import get_connection

router = APIRouter()

@router.get("/", summary="List available disease categories")
def get_disease_list():
    try:
        query = load_query("disease_list.sql")
        con = get_connection()
        result = con.execute(query).fetchall()
        return [
            {"disease_category": row[0], "concept_id": row[1]}
            for row in result
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading disease list: {str(e)}")