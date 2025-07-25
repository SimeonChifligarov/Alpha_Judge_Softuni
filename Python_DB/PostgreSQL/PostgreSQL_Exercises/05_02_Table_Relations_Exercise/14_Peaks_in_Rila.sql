SELECT
    m.mountain_range,
    p.peak_name,
    p.elevation
FROM
    mountains m
JOIN
    peaks p ON m.id = p.mountain_id
WHERE
    m.mountain_range = 'Rila'
ORDER BY
    p.elevation DESC;
