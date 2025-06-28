-- Task: List the number of records for each score in 'second_table', ordered by count descending

-- This query groups records by score and counts how many records per score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

