CREATE OR REPLACE PROCEDURE sp_transfer_money(
    sender_id INT,
    receiver_id INT,
    amount NUMERIC
)
LANGUAGE plpgsql
AS $$
DECLARE
    current_balance NUMERIC;
BEGIN
    SELECT balance INTO current_balance
    FROM accounts
    WHERE id = sender_id;

    IF current_balance >= amount THEN
        CALL sp_withdraw_money(sender_id, amount);
        CALL sp_deposit_money(receiver_id, amount);
    ELSE
        RAISE NOTICE 'Insufficient balance to withdraw %.4f', amount;
    END IF;
END;
$$;
