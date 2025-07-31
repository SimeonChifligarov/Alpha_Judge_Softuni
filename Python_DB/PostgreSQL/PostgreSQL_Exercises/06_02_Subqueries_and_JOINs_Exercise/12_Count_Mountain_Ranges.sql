SELECT
    mc.country_code,
    COUNT(DISTINCT m.mountain_range) AS mountain_range_count
FROM mountains_countries mc
JOIN mountains m ON mc.mountain_id = m.id
WHERE mc.country_code IN ('US', 'RU', 'BG')
GROUP BY mc.country_code
ORDER BY mountain_range_count DESC;
