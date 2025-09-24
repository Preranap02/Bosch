use bosch;
SELECT p.Category_ID,
       AVG(p.Price) AS AvgCategoryPrice
FROM products p
GROUP BY p.Category_ID
HAVING AVG(p.Price) > (
    SELECT AVG(Price) 
    FROM products
);