SELECT
    a.name AS animal,
    EXTRACT(YEAR FROM a.birthdate) AS birth_year,
    at.animal_type
FROM animals a
JOIN animal_types at ON a.animal_type_id = at.id
WHERE a.owner_id IS NULL
  AND a.animal_type_id <> 3
  AND EXTRACT(YEAR FROM AGE(DATE '2022-01-01', a.birthdate)) < 5
ORDER BY animal ASC;
