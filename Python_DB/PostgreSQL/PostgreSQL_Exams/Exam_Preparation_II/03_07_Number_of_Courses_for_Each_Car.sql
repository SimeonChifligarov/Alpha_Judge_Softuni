SELECT
    c.id AS car_id,
    c.make,
    c.mileage,
    COUNT(cs.id) AS count_of_courses,
    ROUND(AVG(cs.bill), 2) AS average_bill
FROM cars c
LEFT JOIN courses cs ON c.id = cs.car_id
GROUP BY c.id, c.make, c.mileage
HAVING COUNT(cs.id) <> 2
ORDER BY count_of_courses DESC, c.id ASC;
