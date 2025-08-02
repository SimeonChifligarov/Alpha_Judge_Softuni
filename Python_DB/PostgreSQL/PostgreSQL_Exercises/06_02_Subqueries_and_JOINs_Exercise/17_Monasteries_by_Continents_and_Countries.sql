UPDATE countries
SET country_name = 'Burma'
WHERE country_name = 'Myanmar';

INSERT INTO monasteries (monastery_name, country_code)
VALUES
('Hanga Abbey', (SELECT country_code FROM countries WHERE country_name = 'Tanzania')),
('Myin-Tin-Daik', (SELECT country_code FROM countries WHERE country_name = 'Myanmar'));

SELECT
    ct.continent_name,
    c.country_name,
    COUNT(m.country_code) AS monasteries_count
FROM continents ct
JOIN countries c USING (continent_code)
LEFT JOIN monasteries m USING (country_code)
WHERE NOT c.three_rivers
GROUP BY c.country_name, ct.continent_name
ORDER BY monasteries_count DESC, c.country_name ASC;
