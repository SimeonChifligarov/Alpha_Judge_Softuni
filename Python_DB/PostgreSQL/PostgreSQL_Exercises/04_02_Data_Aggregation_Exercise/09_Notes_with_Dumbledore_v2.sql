SELECT
    last_name,
    COUNT(*) AS notes_with_dumbledore
FROM
    wizard_deposits
WHERE
    notes ~* '\mDumbledore\M'
GROUP BY
    last_name;
