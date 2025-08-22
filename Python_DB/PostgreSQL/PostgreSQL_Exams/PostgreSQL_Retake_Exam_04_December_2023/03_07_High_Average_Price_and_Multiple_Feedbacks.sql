SELECT
  p."name" AS product_name,
  ROUND(AVG(p.price), 2) AS average_price,
  COUNT(f."id") AS total_feedbacks
FROM
  products AS p
LEFT JOIN
  feedbacks AS f
  ON f.product_id = p."id"
WHERE
  p.price > 15
GROUP BY
  1
HAVING
  COUNT(f."id") > 1
ORDER BY
  3;
