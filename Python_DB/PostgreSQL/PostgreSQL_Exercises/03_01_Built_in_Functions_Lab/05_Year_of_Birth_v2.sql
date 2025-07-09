SELECT
    first_name,
    last_name,
    date_part('year', born) AS year  -- PostgreSQL-specific
FROM
    authors;
