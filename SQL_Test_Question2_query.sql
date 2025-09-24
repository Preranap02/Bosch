use bosch;
SELECT Department_ID, AVG(Salary) AS AvgSalary
FROM employees
GROUP BY Department_ID
ORDER BY AvgSalary DESC
LIMIT 1;