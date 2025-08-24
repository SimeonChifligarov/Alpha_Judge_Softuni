WITH likes_cte AS (
  SELECT photo_id, COUNT(*) AS likes_count
  FROM (SELECT DISTINCT id, photo_id FROM likes) AS l
  GROUP BY photo_id
),
comments_cte AS (
  SELECT photo_id, COUNT(*) AS comments_count
  FROM (SELECT DISTINCT id, photo_id FROM comments) AS c
  GROUP BY photo_id
)
SELECT
  p.id AS photo_id,
  COALESCE(l.likes_count, 0) AS likes_count,
  COALESCE(c.comments_count, 0) AS comments_count
FROM photos AS p
LEFT JOIN likes_cte AS l  ON l.photo_id = p.id
LEFT JOIN comments_cte AS c ON c.photo_id = p.id
ORDER BY likes_count DESC, comments_count DESC, photo_id ASC;
