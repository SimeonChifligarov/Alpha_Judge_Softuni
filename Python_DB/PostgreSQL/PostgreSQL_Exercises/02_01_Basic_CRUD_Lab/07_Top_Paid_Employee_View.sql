-- Create a view for the top-paid employee
CREATE OR REPLACE VIEW top_paid_employee AS
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 1;

-- Select from the view to check the result
SELECT *
FROM top_paid_employee;
