-- Write a script that lists all shows without a genre linked in hbtn_0d_tvshows
-- Each record shows tv_shows.title and NULL for tv_show_genres.genre_id
-- Results sorted by tv_shows.title ASC and tv_show_genres.genre_id ASC (NULLs last)
-- Use only one SELECT statement

SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;

