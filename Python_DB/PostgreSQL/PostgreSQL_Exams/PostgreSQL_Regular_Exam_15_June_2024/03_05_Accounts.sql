SELECT
  a.username,
  a.gender,
  a.age
FROM accounts AS a
WHERE a.age >= 18
  AND CHAR_LENGTH(a.username) > 9
ORDER BY a.age DESC, a.username ASC;
