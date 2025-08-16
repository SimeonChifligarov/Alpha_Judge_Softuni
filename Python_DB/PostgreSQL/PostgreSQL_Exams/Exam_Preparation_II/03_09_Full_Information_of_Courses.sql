SELECT
  a."name" AS address,
  CASE WHEN EXTRACT(HOUR FROM cs."start") BETWEEN 6 AND 20 THEN 'Day' ELSE 'Night' END AS day_time,
  cs.bill,
  cl.full_name,
  ca.make,
  ca.model,
  cat."name" AS category_name
FROM courses cs
JOIN addresses a ON a."id" = cs.from_address_id
JOIN clients cl ON cl."id" = cs.client_id
JOIN cars ca ON ca."id" = cs.car_id
JOIN categories cat ON cat."id" = ca.category_id
ORDER BY cs."id";
