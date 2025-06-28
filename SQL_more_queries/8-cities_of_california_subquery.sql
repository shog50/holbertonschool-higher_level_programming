-- Task: List all cities of California using a subquery (no JOIN), ordered by city id

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;

