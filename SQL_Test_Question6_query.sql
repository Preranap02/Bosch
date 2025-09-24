use bosch;
SELECT p.Product_ID,
       p.Product_Name
FROM products p
LEFT JOIN orders o
    ON p.Product_ID = o.Product_ID
WHERE o.Product_ID IS NULL;
   

