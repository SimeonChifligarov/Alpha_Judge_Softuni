SELECT
    v.driver_id,
    v.vehicle_type,
    CONCAT(c.first_name, ' ', c.last_name) AS driver_name
FROM vehicles v
JOIN campers c ON v.driver_id = c.id;
