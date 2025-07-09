SELECT
    first_name,
    last_name,
    EXTRACT(YEAR FROM born)::INT AS year
FROM
    authors;
