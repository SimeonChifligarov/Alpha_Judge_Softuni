SELECT
  c.name AS country_name,
  COUNT(p.id) AS productions_count,
  COALESCE(AVG(pi.budget), 0) AS avg_budget
FROM countries AS c
LEFT JOIN productions AS p ON p.country_id = c.id
LEFT JOIN productions_info AS pi ON pi.id = p.production_info_id
GROUP BY c.id, c.name
HAVING COUNT(p.id) > 0
ORDER BY productions_count DESC, country_name ASC;
