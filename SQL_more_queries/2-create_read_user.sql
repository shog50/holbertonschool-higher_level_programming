-- Task: Create the database 'hbtn_0d_2' and user 'user_0d_2'
-- user_0d_2 should have only SELECT privilege on 'hbtn_0d_2'
-- Script should not fail if database or user already exists

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if it doesn't exist, with password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege only on hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply privilege changes immediately
FLUSH PRIVILEGES;

