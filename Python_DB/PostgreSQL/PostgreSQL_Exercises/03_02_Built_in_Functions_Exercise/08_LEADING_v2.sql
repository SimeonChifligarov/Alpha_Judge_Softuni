SELECT
    continent_name,
    LTRIM(continent_name) AS "trim"  -- PostgreSQL-specific function
FROM
    continents;
