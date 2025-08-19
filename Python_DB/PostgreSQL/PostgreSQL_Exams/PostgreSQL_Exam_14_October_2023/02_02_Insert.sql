INSERT INTO coaches (first_name, last_name, salary, coach_level)
SELECT
  p.first_name,
  p.last_name,
  p.salary * 2.0,
  CHAR_LENGTH(p.first_name)
FROM players AS p
WHERE p.hire_date < TIMESTAMP '2013-12-13 07:18:46';
