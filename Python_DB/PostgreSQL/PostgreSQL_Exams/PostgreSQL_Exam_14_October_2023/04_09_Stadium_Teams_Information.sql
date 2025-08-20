CREATE OR REPLACE FUNCTION fn_stadium_team_name(p_stadium_name VARCHAR(30))
RETURNS TABLE (team_name VARCHAR(45))
LANGUAGE SQL
AS $fn$
  SELECT t."name" AS team_name
  FROM teams t
  JOIN stadiums s ON s.id = t.stadium_id
  WHERE s."name" = p_stadium_name
  ORDER BY t."name";
$fn$;
