CREATE OR REPLACE PROCEDURE sp_increase_salaries(department_name VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE employees e
    SET salary = salary * 1.05
    FROM departments d
    WHERE e.department_id = d.department_id
      AND d.name = department_name;
END;
$$;
