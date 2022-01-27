--titles of all movies in which both
--Johnny Depp and Helena Bonham Carter starred.

SELECT m.title
FROM movies as m
INNER JOIN stars as s
    ON m.id = s.movie_id
INNER JOIN people as p
    ON s.person_id = p.id
WHERE m.id in (SELECT movies.id
               FROM movies
               INNER JOIN stars ON movies.id = stars.movie_id
               INNER JOIN people ON stars.person_id = people.id
               WHERE people.name = 'Johnny Depp')
    AND p.name = 'Helena Bonham Carter';