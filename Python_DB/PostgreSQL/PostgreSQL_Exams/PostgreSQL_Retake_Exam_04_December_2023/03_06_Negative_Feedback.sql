SELECT
  fb.product_id,
  fb.rate AS "Rate",
  fb.description,
  c.id AS customer_id,
  c.age,
  c.gender
FROM customers AS c
JOIN feedbacks AS fb ON fb.customer_id = c.id
WHERE fb.rate < 5
  AND c.age > 30
  AND c.gender = 'F'
ORDER BY 1 DESC;
