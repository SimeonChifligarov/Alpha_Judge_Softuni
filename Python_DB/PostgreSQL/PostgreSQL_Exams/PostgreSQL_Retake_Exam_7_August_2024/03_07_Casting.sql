SELECT
  a.first_name || ' ' || a.last_name AS full_name,
  lower(left(a.first_name, 1)) || right(a.last_name, 2) || char_length(a.last_name)::text || '@sm-cast.com' AS email,
  a.awards
FROM actors AS a
WHERE NOT EXISTS (
  SELECT 1
  FROM productions_actors AS pa
  WHERE pa.actor_id = a.id
)
ORDER BY a.awards DESC, a.id ASC;
