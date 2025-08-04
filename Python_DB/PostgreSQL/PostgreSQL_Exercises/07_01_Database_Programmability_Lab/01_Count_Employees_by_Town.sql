CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
    result INT;
BEGIN
    SELECT COUNT(*) INTO result
    FROM employees e
    JOIN addresses a ON e.address_id = a.address_id
    JOIN towns t ON a.town_id = t.town_id
    WHERE t.name = town_name;
    RETURN result;
END;
$$;
