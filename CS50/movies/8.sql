--list the names of all people who starred in Toy Story.

SELECT p.name
FROM people as p
INNER JOIN stars as s
    ON p.id = s.person_id
INNER JOIN movies as m
    ON s.movie_id = m.id
WHERE m.title = 'Toy Story';