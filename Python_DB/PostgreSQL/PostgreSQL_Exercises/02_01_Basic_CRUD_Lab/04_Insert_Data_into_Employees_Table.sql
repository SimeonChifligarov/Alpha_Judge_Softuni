-- Insert new employee records
INSERT INTO employees (
    first_name,
    last_name,
    job_title,
    department_id,
    salary
) VALUES
    ('Samantha', 'Young', 'Housekeeping', 4, 900),
    ('Roger', 'Palmer', 'Waiter', 3, 928.33)
;

-- Select all employee data to verify the inserts
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
