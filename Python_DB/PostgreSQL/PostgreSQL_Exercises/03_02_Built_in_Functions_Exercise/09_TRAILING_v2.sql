SELECT
    continent_name,
    RTRIM(continent_name) AS trim  -- PostgreSQL-specific function
FROM
    continents;
