SELECT
    CONCAT_WS(
        ' ',
        elevation,
        '--->>',
        peak_name
    ) AS "Elevation -->> Peak Name"
FROM
    peaks
WHERE
    elevation >= 4884;
