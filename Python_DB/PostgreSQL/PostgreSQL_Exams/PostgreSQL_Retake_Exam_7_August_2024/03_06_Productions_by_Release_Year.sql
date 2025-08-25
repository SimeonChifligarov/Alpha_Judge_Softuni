SELECT
  p.id,
  p.title,
  pi.duration,
  ROUND(pi.budget, 1) AS budget,
  TO_CHAR(pi.release_date, 'MM-YY') AS release_date
FROM productions AS p
JOIN productions_info AS pi
  ON pi.id = p.production_info_id
WHERE pi.release_date >= DATE '2023-01-01'
  AND pi.release_date <= DATE '2024-12-31'
  AND pi.budget > 1500000
ORDER BY 4 ASC, 3 DESC, 1 ASC
LIMIT 3;
