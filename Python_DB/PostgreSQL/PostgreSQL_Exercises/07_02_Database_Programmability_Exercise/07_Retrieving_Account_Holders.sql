CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(searched_balance NUMERIC)
LANGUAGE plpgsql
AS $$
DECLARE
    holder RECORD;
    total_balance NUMERIC;
BEGIN
    FOR holder IN
        SELECT ah.account_holder_id, ah.first_name, ah.last_name
        FROM account_holders ah
        ORDER BY ah.first_name, ah.last_name
    LOOP
        SELECT SUM(a.balance) INTO total_balance
        FROM accounts a
        WHERE a.account_holder_id = holder.account_holder_id;

        IF total_balance > searched_balance THEN
            RAISE NOTICE '% % - %', holder.first_name, holder.last_name, ROUND(total_balance, 4);
        END IF;
    END LOOP;
END;
$$;
