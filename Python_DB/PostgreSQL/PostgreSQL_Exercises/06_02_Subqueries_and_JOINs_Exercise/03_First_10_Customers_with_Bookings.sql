SELECT
    b.booking_id,
    CAST(b.starts_at AS DATE) AS starts_at,
    b.apartment_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM
    bookings b
RIGHT JOIN
    customers c
ON
    b.customer_id = c.customer_id
ORDER BY
    customer_name ASC
LIMIT 10;
