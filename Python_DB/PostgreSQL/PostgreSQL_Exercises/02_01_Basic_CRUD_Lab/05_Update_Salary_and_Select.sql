-- Update salaries of all Managers
UPDATE employees
SET salary = salary + 100
WHERE job_title = 'Manager';

-- Select all Managers to verify the update
SELECT
    id,
    first_name,
    last_name,
    job_title,
    department_id,
    salary
FROM
    employees
WHERE
    job_title = 'Manager'
ORDER BY
    id;
