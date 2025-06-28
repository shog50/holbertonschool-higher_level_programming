-- Task: Create the table 'unique_id' with 'id' INT default 1 and UNIQUE constraint, and 'name' VARCHAR(256)
-- The script should not fail if the table already exists

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

