-- List all genres and the number of shows linked to each
-- Only genres with at least one show are displayed
SELECT g.name AS genre, COUNT(s.id) AS number_of_shows
FROM genres g
JOIN tv_shows s ON g.id = s.genre_id
GROUP BY g.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
