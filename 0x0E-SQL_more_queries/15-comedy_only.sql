-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title 

SELECT t.title
FROM tv_shows t
JOIN tv_show_genres s ON t.id = s.show_id
JOIN tv_genres g ON s.genre_id = g.id AND g.name = 'Comedy'
ORDER BY t.title;
