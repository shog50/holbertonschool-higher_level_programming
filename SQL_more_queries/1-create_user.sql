-- Task: Create MySQL user 'user_0d_1' with all privileges and password 'user_0d_1_pwd'
-- The script should not fail if the user already exists

-- Create the user if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply the privilege changes immediately
FLUSH PRIVILEGES;

