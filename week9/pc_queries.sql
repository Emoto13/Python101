1.SELECT AVG(speed)
FROM PC

2.SELECT maker, AVG(l.screen)
FROM PRODUCT as p
INNER JOIN LAPTOP as l ON p.model = l.model
GROUP BY p.maker

3.SELECT AVG(speed)
FROM LAPTOP
WHERE price > 1000

4.SELECT AVG(price)
FROM PC
GROUP BY hd

5.SELECT AVG(price)
FROM PC
WHERE speed > 500
GROUP BY speed

6.SELECT AVG(p.price)
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

7.1.SELECT *
FROM
(SELECT AVG(price) FROM pc JOIN product ON pc.model=product.model WHERE maker="B"),
(SELECT AVG(price) FROM laptop JOIN product ON laptop.model=product.model WHERE maker="B")

7.2. SELECT ( Sum(pc.price) + Sum(laptop.price) ) / Count(*)
FROM product
LEFT OUTER JOIN pc
ON product.model = pc.model
LEFT OUTER JOIN laptop
ON product.model = laptop.model
WHERE product.maker = 'B'

8.SELECT prod.maker
FROM PRODUCT AS prod
WHERE prod.type = 'PC'
GROUP BY prod.maker
HAVING COUNT(prod.model) >= 3

9.SELECT AVG(price) as avg_price, maker
FROM PC
INNER JOIN PRODUCT as p
ON pc.model = product.model
GROUP BY maker
ORDER BY avg_price DESC

10.SELECT AVG(hd)
FROM PRODUCT AS prod
INNER JOIN PC as p ON p.model = prod.model
WHERE maker in
(SELECT maker from product WHERE type = 'Printer')
