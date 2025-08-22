SELECT
  i."name" AS ingredient_name,
  p."name" AS product_name,
  d."name" AS distributor_name
FROM products_ingredients AS pi
JOIN products AS p ON p."id" = pi.product_id
JOIN ingredients AS i ON i."id" = pi.ingredient_id
JOIN distributors AS d ON d."id" = i.distributor_id AND d.country_id = 16
WHERE i."name" ILIKE '%mustard%'
ORDER BY 2 ASC;
