-- List all genres and the number of shows linked to each
-- Only genres with at least one show are displayed
SELECT
    tg.name AS genre,
    COUNT(tsg.show_id) AS number_of_shows
FROM
    tv_genres tg
INNER JOIN
    tv_show_genres tsg ON tg.id = tsg.genre_id
GROUP BY
    tg.name
ORDER BY
    number_of_shows DESC;
