-- a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name

SELECT t.title, g.name
FROM tv_shows t
LEFT JOIN tv_show_genres s ON t.id = s.show_id
LEFT JOIN tv_genres g ON s.genre_id = g.id
ORDER BY t.title ASC, g.name ASC;
