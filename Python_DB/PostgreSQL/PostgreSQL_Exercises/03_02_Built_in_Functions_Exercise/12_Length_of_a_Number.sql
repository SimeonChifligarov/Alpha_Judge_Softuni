SELECT
    population,
    LENGTH(CAST(population AS TEXT)) AS length
    -- LENGTH(CAST(population AS VARCHAR)) AS "length"
FROM
    countries;
