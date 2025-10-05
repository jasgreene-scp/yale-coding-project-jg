SELECT DISTINCT disease_category, omop_concept_id 
FROM read_csv_auto('app/data/concept_map.csv') 
ORDER BY disease_category;