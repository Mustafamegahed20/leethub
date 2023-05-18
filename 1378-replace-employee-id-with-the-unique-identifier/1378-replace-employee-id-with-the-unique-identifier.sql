/* Write your T-SQL query statement below */

select unique_id,name
from Employees  e
left Join EmployeeUNI s
ON e.id=s.id 