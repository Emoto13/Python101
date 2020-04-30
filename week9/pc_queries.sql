1.SELECT AVG(speed)
FROM PC

2.SELECT maker, AVG(l.screen)
FROM PRODUCT as p
INNER JOIN LAPTOP as l
WHERE p.model = l.model
GROUP BY p.maker

3.SELECT AVG(speed)
FROM LAPTOP
WHERE price > 1000

4.SELECT hd, AVG(price)
FROM PC
GROUP BY hd

5.SELECT AVG(price)
FROM PC
WHERE speed > 500

6.SELECT prod.maker, AVG(p.price)
FROM PC as p
INNER JOIN PRODUCT as prod ON p.model = prod.model
WHERE prod.maker = 'A'


7.SELECT
(((SELECT SUM(p.price)
FROM PC as p
INNER JOIN PRODUCT as prod ON p.model = prod.model
WHERE prod.maker = 'B')
+
(SELECT SUM(l.price)
FROM LAPTOP as l
INNER JOIN PRODUCT as prod ON l.model = prod.model
WHERE prod.maker = 'B'))
/
((SELECT COUNT(l.model)
FROM LAPTOP as l
INNER JOIN PRODUCT as prod ON l.model = prod.model
WHERE prod.maker = 'B')
+
(SELECT COUNT(p.model)
FROM PC as p
INNER JOIN PRODUCT as prod ON p.model = prod.model
WHERE prod.maker = 'B')))
FROM product as prod
LIMIT 1

8.SELECT prod.maker
FROM PRODUCT AS prod
WHERE prod.type = 'PC'
GROUP BY prod.maker
HAVING COUNT(prod.model) >= 3

9.SELECT prod.maker
FROM PRODUCT AS prod
INNER JOIN PC as p
WHERE prod.type = 'PC'
ORDER BY p.price DESC
LIMIT 1

10.SELECT prod.maker, AVG(hd)
FROM PRODUCT AS prod
INNER JOIN PRINTER as prt
INNER JOIN PC as p
WHERE p.model = prod.model
GROUP BY prod.maker
