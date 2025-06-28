-- Write a script that lists all genres of the show "Dexter"
-- Each record displays tv_genres.name
-- Results sorted ascending by genre name
-- Use only one SELECT statement

SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;

