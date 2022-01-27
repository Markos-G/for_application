--lists the names of songs that are by Post Malone.

SELECT name FROM songs as s,
        (SELECT id FROM artists
                WHERE name = 'Post Malone') as p
    WHERE s.artist_id = p.id;