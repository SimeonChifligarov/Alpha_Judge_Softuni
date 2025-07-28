SELECT
    a.name,
    a.country,
    CAST(b.booked_at AS DATE) AS booked_at
FROM
    apartments a
LEFT JOIN
    bookings b
ON
    a.booking_id = b.booking_id
ORDER BY
    a.apartment_id
LIMIT 10;
