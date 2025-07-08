SELECT
    '***' || SUBSTRING(title FROM 4) AS title
FROM
    books
WHERE
    LEFT(title, 3) = 'The'
ORDER BY
    id;
