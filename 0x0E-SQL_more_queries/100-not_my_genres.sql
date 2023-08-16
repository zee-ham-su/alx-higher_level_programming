-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name

SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    SELECT DISTINCT g.id
    FROM tv_genres g
    INNER JOIN tv_show_genres s ON g.id = s.genre_id
    INNER JOIN tv_shows t ON s.show_id = t.id
    WHERE t.title = "Dexter"
) AS linked_genres ON tv_genres.id = linked_genres.id
WHERE linked_genres.id IS NULL
ORDER BY tv_genres.name;
