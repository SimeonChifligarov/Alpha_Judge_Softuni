SELECT
    SUBSTRING("River Information" FROM '([0-9]{1,4})')::INT AS river_length
FROM
    view_river_info;
