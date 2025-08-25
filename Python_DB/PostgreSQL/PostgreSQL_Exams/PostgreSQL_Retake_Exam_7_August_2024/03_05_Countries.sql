SELECT
  c.id,
  c.name,
  c.continent,
  c.currency
FROM countries AS c
WHERE c.continent = 'South America'
  AND LEFT(c.currency, 1) IN ('P', 'U')
ORDER BY c.currency DESC, c.id ASC;
