-- Step 1: Fix existing NULLs (prevent constraint violations)
UPDATE minions_info SET
    age = COALESCE(age, 0),
    name = COALESCE(name, ''),
    code = COALESCE(code, '');

-- Step 2: Set defaults for future inserts
ALTER TABLE minions_info
ALTER COLUMN age SET DEFAULT 0,
ALTER COLUMN name SET DEFAULT '',
ALTER COLUMN code SET DEFAULT '';

-- Step 3: Enforce NOT NULL constraints safely
ALTER TABLE minions_info
ALTER COLUMN age SET NOT NULL,
ALTER COLUMN name SET NOT NULL,
ALTER COLUMN code SET NOT NULL;
