--titles of the five highest rated movies (in order)
--that Chadwick Boseman starred in, starting with the highest rated.

SELECT m.title
FROM movies as m
INNER JOIN ratings as r
    ON m.id = r.movie_id
INNER JOIN stars as s
    ON m.id = s.movie_id
INNER JOIN people as p
    ON s.person_id = p.id
WHERE p.name = 'Chadwick Boseman'
ORDER BY r.rating desc
LIMIT 5;