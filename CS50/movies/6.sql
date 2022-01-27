--average rating of all movies released in 2012.

SELECT AVG(r.rating)
FROM movies as m
INNER JOIN ratings as r
    ON r.movie_id = m.id
WHERE m.year = 2012;
