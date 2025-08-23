DELETE FROM addresses AS a
--WHERE (a.id & 1) = 0
WHERE a.id % 2 = 0
  AND a.street ILIKE '%r%';
