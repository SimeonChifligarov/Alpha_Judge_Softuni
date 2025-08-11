CREATE TABLE IF NOT EXISTS notification_emails (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    recipient_id INT,
    subject TEXT,
    body TEXT
);

CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO notification_emails (
        recipient_id,
        subject,
        body
    )
    VALUES (
        NEW.account_id,
        'Balance change for account: ' || NEW.account_id,
        'On ' || CURRENT_DATE || ' your balance was changed from ' ||
        TO_CHAR(OLD.new_sum, 'FM999999999.0000') || ' to ' ||
        TO_CHAR(NEW.new_sum, 'FM999999999.0000') || '.'
    );
    RETURN NEW;
END;
$$;

CREATE TRIGGER tr_send_email_on_balance_change
AFTER UPDATE ON logs
FOR EACH ROW
WHEN (OLD.new_sum IS DISTINCT FROM NEW.new_sum)
EXECUTE FUNCTION trigger_fn_send_email_on_balance_change();
