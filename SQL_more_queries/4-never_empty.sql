-- Task: Create the table 'id_not_null' with 'id' INT default 1 and 'name' VARCHAR(256)
-- The script should not fail if the table already exists

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

