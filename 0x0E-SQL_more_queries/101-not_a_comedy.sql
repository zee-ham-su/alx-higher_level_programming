-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title

SELECT DISTINCT t.title
FROM tv_shows t
LEFT JOIN tv_show_genres s ON t.id = s.show_id
LEFT JOIN tv_genres g ON s.genre_id = g.id AND g.name = 'Comedy'
WHERE g.id IS NULL
ORDER BY t.title;
