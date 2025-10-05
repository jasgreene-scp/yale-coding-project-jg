import os

def load_query(filename: str) -> str:
    sql_path = os.path.join(os.path.dirname(__file__), '..', 'sql', filename)
    with open(os.path.abspath(sql_path), 'r') as file:
        return file.read()