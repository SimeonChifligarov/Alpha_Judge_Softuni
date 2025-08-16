SELECT
    cl.full_name,
    COUNT(DISTINCT cs.car_id) AS count_of_cars,
    ROUND(SUM(cs.bill), 2) AS total_sum
FROM clients cl
JOIN courses cs ON cl.id = cs.client_id
WHERE SUBSTRING(cl.full_name, 2, 1) = 'a'
GROUP BY cl.full_name
HAVING COUNT(DISTINCT cs.car_id) > 1
ORDER BY cl.full_name ASC;
