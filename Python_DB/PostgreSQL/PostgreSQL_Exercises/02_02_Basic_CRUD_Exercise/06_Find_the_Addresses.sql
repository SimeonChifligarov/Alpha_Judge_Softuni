SELECT
    id,
    -- CONCAT(TRIM(number), ' ', TRIM(street)) AS address,
    CONCAT(number, ' ', street) AS address,
    city_id
FROM
    addresses
WHERE
    id >= 20;
