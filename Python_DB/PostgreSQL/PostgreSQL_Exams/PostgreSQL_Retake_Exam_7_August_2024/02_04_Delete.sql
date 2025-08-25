DELETE FROM countries AS c
WHERE NOT EXISTS (
        SELECT 1
        FROM actors AS a
        WHERE a.country_id = c.id
      )
  AND NOT EXISTS (
        SELECT 1
        FROM productions AS p
        WHERE p.country_id = c.id
      );
