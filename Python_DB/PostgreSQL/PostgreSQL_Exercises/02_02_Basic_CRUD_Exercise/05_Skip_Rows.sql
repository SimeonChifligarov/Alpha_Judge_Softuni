SELECT
    id AS id,
    CONCAT_WS(' ', first_name, middle_name, last_name) AS full_name,
    hire_date
FROM
    employees
ORDER BY
    hire_date ASC
OFFSET 9;
