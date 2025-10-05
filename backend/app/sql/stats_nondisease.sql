SELECT
  COUNT(value_as_number) AS n,
  APPROX_QUANTILE(value_as_number, 0.25) AS p25,
  APPROX_QUANTILE(value_as_number, 0.5) AS median,
  APPROX_QUANTILE(value_as_number, 0.75) AS p75,
  AVG(value_as_number) AS mean
FROM measurement
WHERE measurement_concept_id != {{concept_id}}
  AND value_as_number IS NOT NULL;