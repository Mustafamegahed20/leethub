CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
      SELECT DISTINCT Salary
      FROM Employee e1
      WHERE @N = (
      SELECT COUNT(DISTINCT e2.Salary)
        FROM Employee e2
      WHERE e2.Salary >= e1.Salary
        )
    );
END