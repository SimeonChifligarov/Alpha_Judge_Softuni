CREATE VIEW continent_currency_usage AS
SELECT
    continent_code,
    currency_code,
    currency_usage
FROM (
    SELECT
        continent_code,
        currency_code,
        COUNT(*) AS currency_usage,
        DENSE_RANK() OVER (
            PARTITION BY continent_code
            ORDER BY COUNT(*) DESC
        ) AS usage_rank
    FROM countries
    GROUP BY continent_code, currency_code
    HAVING COUNT(*) > 1
) ranked
WHERE usage_rank = 1
ORDER BY currency_usage DESC;
