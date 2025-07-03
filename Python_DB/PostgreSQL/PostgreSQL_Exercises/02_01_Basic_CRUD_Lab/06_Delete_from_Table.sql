-- Delete employees from departments 1 or 2
DELETE FROM employees
WHERE department_id IN (1, 2);

-- Select all remaining employees to verify the deletion
SELECT
    id,
    first_name,
    last_name,
    job_title,
    department_id,
    salary
FROM
    employees
ORDER BY
    id;
