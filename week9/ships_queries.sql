1.SELECT s.name, c.country, c.numguns,  s.launched
FROM SHIPS as s
INNER JOIN CLASSES as c
WHERE c.class = s.class

2.SELECT s.name,c.class,  c.country, c.numguns,  s.launched
FROM SHIPS as s
INNER JOIN CLASSES as c
WHERE c.class = s.class
OR s.name = c.class

3.SELECT o.ship
FROM OUTCOMES as o
INNER JOIN BATTLES as b
WHERE o.battle = b.name
AND b.date LIKE '%1942%'

4.SELECT DISTINCT s.name, c.country, c.class
FROM SHIPS AS s
INNER JOIN CLASSES as c
ON c.class = s.class
INNER JOIN OUTCOMES as o
ON s.name = o.ship

5.SELECT s.name, o.BATTLE, c.country
FROM SHIPS AS s
INNER JOIN OUTCOMES AS o ON o.ship = s.name
INNER JOIN CLASSES AS c ON c.class = s.class
WHERE NOT s.name = o.ship
