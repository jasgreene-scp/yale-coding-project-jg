import duckdb
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    con = duckdb.connect()
    con.execute("INSTALL httpfs; LOAD httpfs;")
    con.execute("SET s3_region='us-east-1';")

    # S3 views
    con.execute("CREATE VIEW condition_occurrence AS SELECT * FROM read_csv_auto('s3://synpuf-omop/cmsdesynpuf100k/condition_occurrence.csv.gz')")
    con.execute("CREATE VIEW person AS SELECT * FROM read_csv_auto('s3://synpuf-omop/cmsdesynpuf100k/person.csv.gz')")
    con.execute("CREATE VIEW measurement AS SELECT * FROM read_csv_auto('s3://synpuf-omop/cmsdesynpuf100k/measurement.csv.gz')")

    # Local view
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'concept_map.csv'))
    con.execute(f"CREATE VIEW disease_concepts AS SELECT * FROM read_csv_auto('{csv_path}', HEADER=TRUE)")

    logging.info("DuckDB connection and views initialized successfully.")

except Exception as e:
    logging.error(f"DuckDB initialization failed: {e}")
    con = None

def get_connection():
    if con is None:
        raise RuntimeError("DuckDB connection is not available. Check error logs for details.")
    return con