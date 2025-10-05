from fastapi import APIRouter, HTTPException
from app.utils.duckdb_con import get_connection
from app.utils.query_loader import load_query

router = APIRouter()

@router.get("/list")
def get_measurement_dropdown():
    measurements = [
        {"concept_id": 3016723, "name": "Creatinine"},
        {"concept_id": 3000963, "name": "Hemoglobin"},
        {"concept_id": 3004501, "name": "Glucose"},
        {"concept_id": 3012888, "name": "Diastolic Blood Pressure"}
    ]
    return {"measurements": measurements}

@router.get("/age_distribution")
def get_age_distribution(concept_id: int):
    try:
        con = get_connection()
        query = load_query("age_distribution.sql").replace("{{concept_id}}", str(concept_id))
        results = con.execute(query).fetchall()
        return {"age_distribution": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving age distribution: {str(e)}")


@router.get("/sex_distribution")
def get_sex_distribution(concept_id: int):
    try:
        con = get_connection()
        query = load_query("sex_distribution.sql").replace("{{concept_id}}", str(concept_id))
        results = con.execute(query).fetchall()
        return {"sex_distribution": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving sex distribution: {str(e)}")
    
@router.get("/stats")
def get_stats_by_group(concept_id: int):
    try:
        con = get_connection()

        disease_query = load_query("measurement_stats_disease.sql").replace("{{concept_id}}", str(concept_id))
        non_disease_query = load_query("measurement_stats_nondisease.sql").replace("{{concept_id}}", str(concept_id))

        disease_stats = con.execute(disease_query).fetchone()
        non_disease_stats = con.execute(non_disease_query).fetchone()

        return {
            "disease": {
                "n": disease_stats[0],
                "p25": disease_stats[1],
                "median": disease_stats[2],
                "p75": disease_stats[3],
                "mean": disease_stats[4]
            },
            "non_disease": {
                "n": non_disease_stats[0],
                "p25": non_disease_stats[1],
                "median": non_disease_stats[2],
                "p75": non_disease_stats[3],
                "mean": non_disease_stats[4]
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving stats: {str(e)}")
    
@router.get("/box-plot")
def box_plot(disease_id: int, measurement_id: int):
    try:
        con = get_connection()
        query_template = load_query("box_plot.sql")
        query = (
            query_template
            .replace("{{DISEASE_ID}}", str(disease_id))
            .replace("{{MEASUREMENT_ID}}", str(measurement_id))
        )
        rows = con.execute(query).fetchall()
        return [{"cohort_type": row[0], "value": row[1]} for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running box plot query: {str(e)}")