CREATE VIEW view_wizard_deposits_with_expiration_date_before_1983_08_17 AS
SELECT DISTINCT
    CONCAT_WS(' ', first_name, last_name) AS wizard_name,
    deposit_start_date AS start_date,
    deposit_expiration_date AS expiration_date,
    deposit_amount AS amount
FROM
    wizard_deposits
WHERE
    deposit_expiration_date <= '1983-08-17'
ORDER BY
    expiration_date ASC;
