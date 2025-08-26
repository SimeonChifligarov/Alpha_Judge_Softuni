CREATE OR REPLACE FUNCTION udf_category_productions_count(category_name VARCHAR(50))
RETURNS VARCHAR
LANGUAGE SQL
AS $$
  SELECT 'Found ' || COUNT(cp.production_id) || ' productions.'
  FROM categories c
  LEFT JOIN categories_productions cp ON cp.category_id = c.id
  WHERE c.name = category_name
$$;
