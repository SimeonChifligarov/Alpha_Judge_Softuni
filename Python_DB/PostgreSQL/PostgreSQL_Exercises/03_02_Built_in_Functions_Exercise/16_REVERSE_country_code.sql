UPDATE
    countries
SET
    country_code = REVERSE(LOWER(country_code));
    -- country_code = LOWER(REVERSE(country_code));  -- less readable
