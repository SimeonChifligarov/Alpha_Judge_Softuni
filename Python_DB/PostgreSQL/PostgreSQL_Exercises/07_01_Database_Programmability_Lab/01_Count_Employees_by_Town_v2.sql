CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
    town_count INT;
BEGIN
    SELECT COUNT(*) INTO town_count
    FROM employees e
    JOIN addresses a USING (address_id)
    JOIN towns t USING (town_id)
    WHERE t.name = town_name;
    RETURN town_count;
END;
$$;
