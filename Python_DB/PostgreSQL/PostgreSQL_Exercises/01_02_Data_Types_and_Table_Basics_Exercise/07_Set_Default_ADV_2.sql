BEGIN;

-- Step 1: Fix existing NULLs explicitly and only if needed
UPDATE minions_info
SET age = 0
WHERE age IS NULL;

UPDATE minions_info
SET name = ''
WHERE name IS NULL;

UPDATE minions_info
SET code = ''
WHERE code IS NULL;

-- Step 2: Set defaults for future inserts
ALTER TABLE minions_info
ALTER COLUMN age SET DEFAULT 0,
ALTER COLUMN name SET DEFAULT '',
ALTER COLUMN code SET DEFAULT '';

-- Step 3: Enforce NOT NULL constraints (only after ensuring data consistency)
ALTER TABLE minions_info
ALTER COLUMN age SET NOT NULL,
ALTER COLUMN name SET NOT NULL,
ALTER COLUMN code SET NOT NULL;

COMMIT;
