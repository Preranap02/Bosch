use bosch;
SELECT o.region,
       o.Customer_ID,
       COUNT(o.Order_ID) AS TotalOrders
FROM orders o
GROUP BY o.region, o.Customer_ID
HAVING COUNT(o.Order_ID) = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(o2.Order_ID) AS cnt
        FROM orders o2
        WHERE o2.region = o.region
        GROUP BY o2.Customer_ID
    ) AS region_counts
);
