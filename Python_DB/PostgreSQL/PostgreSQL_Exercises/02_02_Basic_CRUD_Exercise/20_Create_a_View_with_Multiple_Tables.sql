CREATE VIEW
    view_addresses
AS
SELECT
    CONCAT(e.first_name, ' ', e.last_name) AS full_name,
    e.department_id,
    CONCAT(a.number, ' ', a.street) AS address
FROM
    employees AS e
JOIN
    addresses AS a
    ON e.address_id = a.id
ORDER BY
    address;
