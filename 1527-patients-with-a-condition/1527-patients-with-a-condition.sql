/* Write your T-SQL query statement below */
SELECT *
FROM Patients
WHERE conditions LIKE 'DIAB1%' or conditions LIKE '% DIAB1%'

