SELECT
    peak_name,
    SUBSTRING(peak_name FROM 1 FOR 4) AS positive_left,
    -- SUBSTRING(peak_name FROM 1 FOR LENGTH(peak_name) - 4) AS negative_left  -- negative substring length not allowed
    LEFT(peak_name, -4) AS negative_left
FROM
    peaks;
