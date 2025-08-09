CREATE OR REPLACE PROCEDURE sp_withdraw_money(
    account_id INT,
    money_amount NUMERIC(19,4)
)
LANGUAGE plpgsql
AS $$
DECLARE
    current_balance NUMERIC(19,4);
BEGIN
    SELECT balance INTO current_balance
    FROM accounts
    WHERE id = account_id;

    IF current_balance >= money_amount THEN
        UPDATE accounts
        SET balance = balance - money_amount
        WHERE id = account_id;
        COMMIT;
    ELSE
        RAISE NOTICE 'Insufficient balance to withdraw %.4f', money_amount;
    END IF;
END;
$$;
