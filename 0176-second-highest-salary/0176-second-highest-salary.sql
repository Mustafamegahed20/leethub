/* Write your T-SQL query statement below */
select Max(salary) as  SecondHighestSalary
from employee
where salary <(select MAX(salary) from Employee);