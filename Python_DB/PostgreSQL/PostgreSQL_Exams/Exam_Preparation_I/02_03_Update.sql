UPDATE animals
SET owner_id = (
    SELECT id FROM owners
    WHERE name = 'Kaloqn Stoqnov'
    LIMIT 1
)
WHERE owner_id IS NULL;
