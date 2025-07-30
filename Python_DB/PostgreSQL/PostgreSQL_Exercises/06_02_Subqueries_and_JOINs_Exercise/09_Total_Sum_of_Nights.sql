SELECT
    a.name,
    SUM(b.booked_for) AS sum
FROM apartments a
JOIN bookings b USING (apartment_id)
GROUP BY a.name
ORDER BY a.name ASC;
