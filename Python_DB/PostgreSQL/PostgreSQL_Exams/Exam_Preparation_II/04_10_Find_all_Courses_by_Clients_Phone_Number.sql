CREATE OR REPLACE FUNCTION fn_courses_by_client(phone_num VARCHAR(20))
RETURNS INT AS
$$
DECLARE
    courses_count INT;
BEGIN
    SELECT COUNT(*)
    INTO courses_count
    FROM courses cs
    JOIN clients cl ON cl.id = cs.client_id
    WHERE cl.phone_number = phone_num;

    RETURN courses_count;
END;
$$
LANGUAGE plpgsql;
