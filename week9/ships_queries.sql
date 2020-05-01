1.SELECT s.name, c.country, c.numguns,  s.launched
FROM SHIPS as s
INNER JOIN CLASSES as c ON c.class = s.class

2.SELECT s.name,c.class,  c.country, c.numguns,  s.launched
FROM CLASSES as c
LEFT JOIN SHIPS as s
ON s.name = c.class
WHERE c.class
LIKE (SELECT name FROM ships)
OR s.name IS NOT NULL

3.SELECT o.ship
FROM OUTCOMES as o
INNER JOIN BATTLES as b ON o.battle = b.name
WHERE b.date LIKE '%1942%'

4.SELECT DISTINCT s.name, c.country, c.class
FROM SHIPS AS s
INNER JOIN CLASSES as c
ON c.class = s.class
INNER JOIN OUTCOMES as o
ON s.name = o.ship

5.SELECT s.name
FROM SHIPS AS s
WHERE s.name NOT IN
(SELECT ship
FROM OUTCOMES as o
INNER JOIN BATTLES as b
ON o.battles = b.name)
