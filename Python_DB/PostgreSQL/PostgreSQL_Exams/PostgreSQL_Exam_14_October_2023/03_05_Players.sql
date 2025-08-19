SELECT
  p.first_name || ' ' || p.last_name AS "full_name",
  p.age,
  p.hire_date
FROM players AS p
WHERE p.first_name LIKE 'M%'
ORDER BY 2 DESC, 1 ASC;
