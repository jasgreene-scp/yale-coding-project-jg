SELECT 'disease' AS cohort_type, m.measurement_value
FROM measurement m
JOIN disease_cohort dc ON m.person_id = dc.person_id
WHERE m.measurement_concept_id = {{measurement_id}}
  AND dc.condition_concept_id = {{disease_id}}

UNION ALL

SELECT 'non_disease' AS cohort_type, m.measurement_value
FROM measurement m
WHERE m.person_id NOT IN (
  SELECT person_id FROM disease_cohort WHERE condition_concept_id = {{disease_id}}
)
AND m.measurement_concept_id = {{measurement_id}};