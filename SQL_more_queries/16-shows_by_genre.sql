-- Write a script that lists all shows and all genres linked to that show,
-- display NULL if a show has no genre
-- Display tv_shows.title and tv_genres.name
-- Results sorted ascending by show title and genre name
-- Use only one SELECT statement

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

