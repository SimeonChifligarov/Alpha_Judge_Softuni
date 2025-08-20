WITH coach_names AS (
  SELECT c.id AS coach_id, c.first_name || ' ' || c.last_name AS coach_full_name
  FROM coaches AS c
),
player_info AS (
  SELECT p.id AS player_id,
         p.first_name || ' ' || p.last_name AS player_full_name,
         p.team_id,
         p.skills_data_id
  FROM players AS p
)
SELECT
  cn.coach_full_name,
  pi.player_full_name,
  t."name" AS team_name,
  s."passing",
  s.shooting,
  s.speed
FROM players_coaches AS pc
JOIN coach_names AS cn ON cn.coach_id = pc.coach_id
JOIN player_info AS pi ON pi.player_id = pc.player_id
JOIN skills_data AS s ON s.id = pi.skills_data_id
JOIN teams AS t ON t.id = pi.team_id
ORDER BY 1 ASC, 2 DESC;
