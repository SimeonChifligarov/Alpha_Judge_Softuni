SELECT
  p.title,
  CASE
    WHEN pi.rating <= 3.50 THEN 'poor'
    WHEN pi.rating <= 8.00 THEN 'good'
    ELSE 'excellent'
  END AS rating,
  CASE WHEN pi.has_subtitles IS TRUE THEN 'Bulgarian' ELSE 'N/A' END AS subtitles,
  COUNT(pa.actor_id) AS actors_count
FROM productions AS p
JOIN productions_info AS pi ON pi.id = p.production_info_id
LEFT JOIN productions_actors AS pa ON pa.production_id = p.id
GROUP BY p.title, pi.rating, pi.has_subtitles
ORDER BY 2 ASC, 4 DESC, 1 ASC;
