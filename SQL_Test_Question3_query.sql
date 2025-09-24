use bosch;
SELECT e.Employee_ID,
       e.Name,
       e.Department_ID,
       e.Salary
FROM employees e
WHERE e.Salary > (
    SELECT AVG(e2.Salary)
    FROM employees e2
    WHERE e2.Department_ID = e.Department_ID
);
