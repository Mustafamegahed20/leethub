CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        SELECT DISTINCT Salary
        FROM (
          SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) as rank
          FROM Employee
        ) as ranks
        WHERE rank = @N
    );
END