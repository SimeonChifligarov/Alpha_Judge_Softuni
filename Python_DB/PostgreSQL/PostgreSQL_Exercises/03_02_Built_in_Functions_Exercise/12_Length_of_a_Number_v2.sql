SELECT
    population,
    CASE
        WHEN population = 0 THEN 1
        WHEN population IS NULL THEN NULL
        ELSE FLOOR(LOG(10, population)) + 1
    END AS length
FROM
    countries;
