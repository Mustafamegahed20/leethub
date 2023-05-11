/* Write your T-SQL query statement below */
update Salary
set sex = CASE
    WHEN sex ='m' THEN 'f'
    WHEN sex ='f' THEN 'm'
END



