CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
    IN animal_name VARCHAR(30),
    OUT owner_name TEXT
)
AS $$
BEGIN
    SELECT
        COALESCE(o.name, 'For adoption')
    INTO owner_name
    FROM animals a
    LEFT JOIN owners o
        ON a.owner_id = o.id
    WHERE a.name = animal_name;
END;
$$ LANGUAGE plpgsql;
