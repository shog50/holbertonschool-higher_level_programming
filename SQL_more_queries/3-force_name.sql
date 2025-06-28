-- Task: Create the table 'force_name' with columns id (INT) and name (VARCHAR(256) NOT NULL)
-- The script should not fail if the table already exists

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

