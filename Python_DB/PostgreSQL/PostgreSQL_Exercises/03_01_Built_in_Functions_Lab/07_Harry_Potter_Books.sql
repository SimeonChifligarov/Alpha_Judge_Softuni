SELECT
    title
FROM
    books
WHERE
    -- title LIKE 'Harry Potter%'
    title LIKE '%Harry Potter%'
ORDER BY
    id;
