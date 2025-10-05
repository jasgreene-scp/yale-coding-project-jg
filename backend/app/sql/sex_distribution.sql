SELECT
  CASE gender_concept_id
    WHEN 8507 THEN 'Male'
    WHEN 8532 THEN 'Female'
    ELSE 'Unknown'
  END AS gender,
  COUNT(*) AS n
FROM measurement m
JOIN person p ON m.person_id = p.person_id
WHERE m.measurement_concept_id = {{concept_id}}
  AND m.value_as_number IS NOT NULL
  AND gender_concept_id IN (8507, 8532)
GROUP BY gender
ORDER BY gender;