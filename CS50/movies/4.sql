--determine the number of movies with an IMDb rating of 10.0.

SELECT COUNT(*)
FROM ratings as r
INNER JOIN movies as m
    ON m.id = r.movie_id
WHERE r.rating = 10.0