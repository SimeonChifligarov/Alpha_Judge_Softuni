CREATE OR REPLACE FUNCTION fn_cash_in_users_games(game_name VARCHAR(50))
RETURNS TABLE(total_cash NUMERIC)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT ROUND(SUM(cash), 2) AS total_cash
    FROM (
        SELECT cash,
               ROW_NUMBER() OVER (ORDER BY cash DESC) AS rn
        FROM users_games ug
        JOIN games g ON ug.game_id = g.id
        WHERE g.name = game_name
    ) AS ranked
    WHERE rn % 2 = 1;
END;
$$;
