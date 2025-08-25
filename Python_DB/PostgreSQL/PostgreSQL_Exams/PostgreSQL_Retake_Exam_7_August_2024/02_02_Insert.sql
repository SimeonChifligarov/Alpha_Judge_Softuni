INSERT INTO actors (first_name, last_name, birthdate, height, awards, country_id)
SELECT
    REVERSE(first_name) AS first_name,
    REVERSE(last_name) AS last_name,
    birthdate - INTERVAL '2 days' AS birthdate,
    COALESCE(height, 0) + 10 AS height,
    country_id AS awards,
    (SELECT id FROM countries WHERE name = 'Armenia') AS country_id
FROM
    actors
WHERE
    id BETWEEN 10 AND 20;

--WITH armenia AS (
--  SELECT id
--  FROM countries
--  WHERE name = 'Armenia'
--  LIMIT 1
--)
--INSERT INTO actors (first_name, last_name, birthdate, height, awards, country_id)
--SELECT
--  REVERSE(a.first_name),
--  REVERSE(a.last_name),
--  a.birthdate - make_interval(days => 2),
--  COALESCE(a.height, 0) + 10,
--  a.country_id,
--  ar.id
--FROM actors AS a
--CROSS JOIN armenia AS ar
--WHERE a.id BETWEEN 10 AND 20;
