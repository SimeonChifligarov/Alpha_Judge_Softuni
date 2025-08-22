CREATE OR REPLACE PROCEDURE sp_customer_country_name(
  IN customer_full_name VARCHAR(50),
  OUT country_name VARCHAR(50)
)
LANGUAGE plpgsql
AS $$
BEGIN
  SELECT c."name"
  INTO country_name
  FROM countries c
  JOIN customers cust ON cust.country_id = c."id"
  WHERE (cust.first_name || ' ' || cust.last_name) = customer_full_name
  LIMIT 1;
END;
$$;
