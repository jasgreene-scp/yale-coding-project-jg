WITH disease_concept AS (
  SELECT omop_concept_id
  FROM disease_concepts
  WHERE disease_category = '{{DISEASE_NAME}}'
),
disease_group AS (
  SELECT DISTINCT person_id
  FROM condition_occurrence
  WHERE condition_concept_id IN (SELECT omop_concept_id FROM disease_concept)
),
nondisease_group AS (
  SELECT DISTINCT person_id
  FROM person
  WHERE person_id NOT IN (SELECT person_id FROM disease_group)
)

SELECT 'disease' AS group_type, COUNT(*) AS count FROM disease_group
UNION ALL
SELECT 'nondisease' AS group_type, COUNT(*) AS count FROM nondisease_group;