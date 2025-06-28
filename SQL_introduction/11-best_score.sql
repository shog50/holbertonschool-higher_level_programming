-- Task: List all records with a score >= 10 from 'second_table' ordered by score (highest first)

-- This query selects score and name from second_table where score >= 10, ordered by score descending
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

