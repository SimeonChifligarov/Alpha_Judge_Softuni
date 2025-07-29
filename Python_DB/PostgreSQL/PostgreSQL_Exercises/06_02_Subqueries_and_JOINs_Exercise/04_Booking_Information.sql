SELECT
    b.booking_id,
    a.name AS apartment_owner,
    a.apartment_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM
    bookings b
FULL JOIN
    apartments a ON b.booking_id = a.booking_id
FULL JOIN
    customers c ON b.customer_id = c.customer_id
ORDER BY
    booking_id ASC,
    apartment_owner ASC,
    customer_name ASC;
