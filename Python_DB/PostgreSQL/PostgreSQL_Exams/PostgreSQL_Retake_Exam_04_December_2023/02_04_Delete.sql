DELETE FROM products_ingredients pi
USING ingredients i
JOIN distributors d ON d.id = i.distributor_id
WHERE pi.ingredient_id = i.id
  AND d."name" LIKE 'L%';

DELETE FROM ingredients i
USING distributors d
WHERE i.distributor_id = d.id
  AND d."name" LIKE 'L%';

DELETE FROM distributors
WHERE "name" LIKE 'L%';
