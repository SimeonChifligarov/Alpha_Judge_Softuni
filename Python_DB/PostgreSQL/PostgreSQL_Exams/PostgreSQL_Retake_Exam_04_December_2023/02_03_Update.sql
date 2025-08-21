UPDATE products AS p
SET price = p.price * 1.10
FROM (
  SELECT DISTINCT product_id
  FROM feedbacks
  WHERE rate > 8
) AS q
WHERE q.product_id = p.id;
