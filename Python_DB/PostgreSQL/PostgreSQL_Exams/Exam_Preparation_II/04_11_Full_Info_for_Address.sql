CREATE TABLE IF NOT EXISTS search_results (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  address_name VARCHAR(100),
  full_name VARCHAR(100),
  level_of_bill VARCHAR(20),
  make VARCHAR(30),
  "condition" CHAR(1),
  category_name VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE sp_courses_by_address(address_name VARCHAR(100))
LANGUAGE plpgsql
AS
$$
BEGIN
  TRUNCATE TABLE search_results;

  INSERT INTO search_results (address_name, full_name, level_of_bill, make, "condition", category_name)
  SELECT
    a."name",
    cl.full_name,
    CASE
      WHEN cs.bill <= 20 THEN 'Low'
      WHEN cs.bill <= 30 THEN 'Medium'
      ELSE 'High'
    END,
    ca.make,
    ca."condition",
    cat."name"
  FROM courses cs
  JOIN addresses a ON cs.from_address_id = a."id"
  JOIN clients cl ON cs.client_id = cl."id"
  JOIN cars ca ON cs.car_id = ca."id"
  JOIN categories cat ON ca.category_id = cat."id"
  WHERE a."name" = address_name
  ORDER BY ca.make, cl.full_name;
END;
$$;
