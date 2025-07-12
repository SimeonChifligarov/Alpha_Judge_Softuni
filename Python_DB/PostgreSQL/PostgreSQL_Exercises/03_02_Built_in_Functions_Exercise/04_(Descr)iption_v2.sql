SELECT
    RIGHT(description, -4) AS substring  -- PostgreSQL-specific syntax
FROM
    currencies;
