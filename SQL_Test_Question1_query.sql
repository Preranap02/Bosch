use bosch;
SELECT
    category_id,
    product_id,
    product_name,
    total_sales
FROM (
    SELECT
        s.category_id,
        s.product_id,
        p.product_name,
        SUM(s.sales_amount) AS total_sales,
        RANK() OVER (PARTITION BY s.category_id ORDER BY SUM(s.sales_amount) DESC) AS sales_rank
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY s.category_id, s.product_id, p.product_name
) ranked_sales
WHERE sales_rank = 1;
