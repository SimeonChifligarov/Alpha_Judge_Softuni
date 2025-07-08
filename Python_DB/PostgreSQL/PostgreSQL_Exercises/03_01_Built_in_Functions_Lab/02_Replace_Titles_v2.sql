SELECT
    '***' || SUBSTRING(title FROM 4) AS title
FROM
    books
WHERE
    title LIKE 'The%'
ORDER BY
    id;
