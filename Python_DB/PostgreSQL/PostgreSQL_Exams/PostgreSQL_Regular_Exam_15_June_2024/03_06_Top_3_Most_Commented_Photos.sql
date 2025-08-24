WITH cc AS (
  SELECT photo_id, COUNT(*) AS comments_count
  FROM comments
  GROUP BY photo_id
)
SELECT
  p.id AS photo_id,
  p.capture_date,
  p.description,
  cc.comments_count
FROM cc
JOIN photos AS p ON p.id = cc.photo_id
WHERE p.description IS NOT NULL
ORDER BY cc.comments_count DESC, p.id ASC
LIMIT 3;
