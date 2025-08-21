SELECT
  p.name,
  p.recipe,
  p.price
FROM products AS p
WHERE p.price >= 10 AND p.price <= 20
ORDER BY p.price DESC;
