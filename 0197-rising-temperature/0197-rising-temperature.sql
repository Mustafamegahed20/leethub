/* Write your T-SQL query statement below */

SELECT w2.Id 
FROM Weather w1
INNER JOIN Weather w2 ON DATEDIFF(day, w1.recordDate, w2.recordDate)=1 AND w2.Temperature > w1.Temperature