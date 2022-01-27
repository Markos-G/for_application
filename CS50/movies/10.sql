--people who have directed a movie that received a rating of at least 9.0.

SELECT DISTINCT(p.name)
FROM people as p
INNER JOIN directors as d
    ON p.id = d.person_id
iNNER JOIN movies as m
    ON d.movie_id = m.id
INNER JOIN ratings as r
    ON m.id = r.movie_id
WHERE r.rating >= 9.0;