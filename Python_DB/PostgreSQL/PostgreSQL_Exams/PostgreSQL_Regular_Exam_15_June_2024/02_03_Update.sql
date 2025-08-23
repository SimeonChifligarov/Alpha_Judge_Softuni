UPDATE addresses AS a
SET country = m.new_country
FROM (VALUES
  ('B','Blocked'),
  ('T','Test'),
  ('P','In Progress')
) AS m(prefix, new_country)
WHERE LEFT(a.country, 1) = m.prefix;
