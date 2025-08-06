CREATE OR REPLACE FUNCTION fn_full_name(
    first_name VARCHAR(50),
    last_name VARCHAR(50)
) RETURNS VARCHAR(101)
LANGUAGE plpgsql
AS $$
BEGIN
    IF first_name IS NULL AND last_name IS NULL THEN
        RETURN NULL;
    ELSIF first_name IS NULL THEN
        RETURN INITCAP(LOWER(last_name));
    ELSIF last_name IS NULL THEN
        RETURN INITCAP(LOWER(first_name));
    ELSE
        RETURN INITCAP(LOWER(first_name)) || ' ' || INITCAP(LOWER(last_name));
    END IF;
END;
$$;
