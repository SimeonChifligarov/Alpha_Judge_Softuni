SELECT
    title
FROM
    books
WHERE
    LEFT(title, 3) = 'The'
ORDER BY
    id;
