SELECT
    v.driver_id,
    v.vehicle_type,
    CONCAT(c.first_name, ' ', c.last_name) AS driver_name
FROM vehicles AS v
JOIN campers AS c ON v.driver_id = c.id
WHERE v.driver_id IS NOT NULL;
