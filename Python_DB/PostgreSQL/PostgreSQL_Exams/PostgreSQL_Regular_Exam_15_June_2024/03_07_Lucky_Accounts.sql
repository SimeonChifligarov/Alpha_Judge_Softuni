SELECT
  format('%s %s', a.id, a.username) AS id_username,
  a.email
FROM accounts AS a
WHERE EXISTS (
  SELECT 1
  FROM accounts_photos AS ap
  JOIN photos AS p ON p.id = ap.photo_id
  WHERE ap.account_id = a.id
    AND p.id = a.id
)
ORDER BY a.id ASC;
