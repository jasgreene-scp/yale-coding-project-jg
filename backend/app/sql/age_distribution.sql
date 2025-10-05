SELECT
  CASE
    WHEN CAST(strftime('%Y', m.measurement_date) AS INTEGER) - p.year_of_birth < 20 THEN '0–19'
    WHEN CAST(strftime('%Y', m.measurement_date) AS INTEGER) - p.year_of_birth BETWEEN 20 AND 39 THEN '20–39'
    WHEN CAST(strftime('%Y', m.measurement_date) AS INTEGER) - p.year_of_birth BETWEEN 40 AND 59 THEN '40–59'
    ELSE '60+'
  END AS age_group,
  COUNT(*) AS n
FROM measurement m
JOIN person p ON m.person_id = p.person_id
WHERE m.measurement_concept_id = {{concept_id}}
  AND m.value_as_number IS NOT NULL
GROUP BY age_group
ORDER BY age_group;