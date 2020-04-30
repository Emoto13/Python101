1.SELECT address
FROM STUDIO
WHERE name = 'MGM'

2.SELECT birthdate
FROM MOVIESTAR
WHERE name = 'Kim Basinger'

3.SELECT name
FROM MOVIEEXEC
WHERE networth > 10000000

4.SELECT name
FROM MOVIESTAR
WHERE gender = 'M' OR address = 'Prefect Rd.'

5.INSERT INTO MOVIESTAR (name, address, gender, birthdate)
VALUES ('Zahari Baharov', 'bul. Slivnica', 'M', DATE('1973-10-06'))

6.DELETE FROM STUDIO
WHERE address LIKE '%5%'

7.UPDATE MOVIE
SET studioname = 'Fox'
WHERE title LIKE '%Star%'

8.SELECT m.name
FROM MOVIESTAR as m
INNER JOIN STARSIN as s
ON m.name = s.starname
WHERE m.gender = 'M'
AND s.movietitle = 'Terms of Endearment'

9.SELECT s.starname
FROM STARSIN as s
INNER JOIN MOVIE as m
ON s.movieyear = m.year
WHERE m.year = 1995
AND m.studioname = 'MGM'

10.ALTER TABLE STUDIO
ADD president VARCHAR(50) NOT NULL

11.UPDATE STUDIO
SET president = 'Boyko Borisov'
WHERE name = 'MGM'

12.SELECT president
FROM STUDIO
WHERe name = 'MGM'
