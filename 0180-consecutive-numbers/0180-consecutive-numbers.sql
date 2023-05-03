/* Write your T-SQL query statement below */
SELECT DISTINCT num as ConsecutiveNums 
FROM (
    SELECT num, LEAD(num, 1) OVER (ORDER BY id) AS next1, LEAD(num, 2) OVER (ORDER BY id) AS next2
    FROM Logs 
) l
WHERE num = next1 AND num = next2;
