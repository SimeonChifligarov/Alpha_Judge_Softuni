SELECT
    c.country_name,
    r.river_name
FROM countries c
LEFT JOIN countries_rivers cr USING (country_code)
LEFT JOIN rivers r ON cr.river_id = r.id
WHERE c.continent_code = 'AF'
ORDER BY c.country_name ASC
LIMIT 5;
