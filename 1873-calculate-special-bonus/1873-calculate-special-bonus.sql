/* Write your T-SQL query statement below */
SELECT employee_id,
       CASE 
          WHEN employee_id % 2 = 1 AND Left(name,1) != 'M' THEN salary
          ELSE 0
       END AS bonus
FROM employees
ORDER BY employee_id;