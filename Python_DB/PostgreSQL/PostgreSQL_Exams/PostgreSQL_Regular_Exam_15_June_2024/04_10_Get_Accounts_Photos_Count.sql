CREATE OR REPLACE FUNCTION udf_accounts_photos_count(account_username VARCHAR(30))
RETURNS INT
LANGUAGE SQL
STABLE
AS $$
  SELECT COUNT(*)
  FROM accounts_photos ap
  JOIN accounts a ON a.id = ap.account_id
  WHERE a.username = account_username
$$;
