CREATE OR REPLACE PROCEDURE udp_awarded_production(production_title VARCHAR(70))
LANGUAGE plpgsql
AS $$
BEGIN
  UPDATE actors AS a
  SET awards = a.awards + 1
  FROM productions AS p
  JOIN productions_actors AS pa ON pa.production_id = p.id
  WHERE a.id = pa.actor_id
    AND p.title = production_title;
END;
$$;
