CREATE OR REPLACE PROCEDURE sp_players_team_name(
  IN player_name VARCHAR(50),
  OUT team_name VARCHAR(45)
)
LANGUAGE plpgsql
AS $$
BEGIN
  SELECT COALESCE(t.name, 'The player currently has no team')
  INTO team_name
  FROM players p
  LEFT JOIN teams t ON t.id = p.team_id
  WHERE (p.first_name || ' ' || p.last_name) = player_name
  LIMIT 1;

  IF NOT FOUND THEN
    team_name := 'The player currently has no team';
  END IF;
END;
$$;
