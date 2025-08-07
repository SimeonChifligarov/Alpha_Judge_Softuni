CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    set_of_letters VARCHAR(50),
    word VARCHAR(50)
) RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
DECLARE
    i INT := 1;
    letter CHAR;
    letters TEXT := LOWER(REGEXP_REPLACE(set_of_letters, '[^a-z]', '', 'g'));
    cleaned_word TEXT := LOWER(REGEXP_REPLACE(word, '[^a-z]', '', 'g'));
BEGIN
    WHILE i <= LENGTH(cleaned_word) LOOP
        letter := SUBSTRING(cleaned_word FROM i FOR 1);
        IF POSITION(letter IN letters) = 0 THEN
            RETURN FALSE;
        END IF;
        letters := OVERLAY(letters PLACING '' FROM POSITION(letter IN letters) FOR 1);
        i := i + 1;
    END LOOP;
    RETURN TRUE;
END;
$$;
