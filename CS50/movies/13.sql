--names of all people who starred in a movie
--in which Kevin Bacon also starred.

SELECT p.name
FROM people as p
INNER JOIN stars as s
    ON p.id = s.person_id
INNER JOIN movies as m
    ON s.movie_id = m.id
WHERE m.id IN (SELECT movies.id
              FROM movies
              INNER JOIN stars
                  ON movies.id=stars.movie_id
              INNER JOIN people
                  ON people.id= stars.person_id
              WHERE people.name = 'Kevin Bacon' AND people.birth = 1958)
    AND p.name != 'Kevin Bacon';