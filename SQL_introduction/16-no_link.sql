-- Task: List all records from 'second_table' where name is not empty or NULL, ordered by score descending

-- This query selects score and name, skips empty or NULL names, and orders by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

