-- Write a script that lists all shows in the database hbtn_0d_tvshows
-- Each record shows tv_shows.title and tv_show_genres.genre_id
-- Shows without genres should show NULL in genre_id
-- Results sorted by tv_shows.title ASC and tv_show_genres.genre_id ASC

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

