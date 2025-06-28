-- Task: Create the database 'hbtn_0d_usa' and table 'states'
-- The table 'states' should have an auto-incrementing 'id' as a unique primary key and a non-null 'name'

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

