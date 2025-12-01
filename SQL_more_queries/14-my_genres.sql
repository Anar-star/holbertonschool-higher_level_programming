-- Select all genres of the show 'Dexter'
-- The database is passed as an argument, so we don't use USE statements
-- Only one SELECT statement is used as required

SELECT genres.name
FROM tv_shows
-- Join with tv_show_genres to get genre IDs linked to the show
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Join with genres table to get the genre names
JOIN genres ON tv_show_genres.genre_id = genres.id
-- Filter for the show Dexter
WHERE tv_shows.title = 'Dexter'
-- Sort genres alphabetically
ORDER BY genres.name ASC;
