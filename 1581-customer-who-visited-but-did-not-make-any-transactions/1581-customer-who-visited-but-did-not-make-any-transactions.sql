/* Write your T-SQL query statement below */
SELECT customer_id, COUNT(isnull(transaction_id, 1)) AS count_no_trans
FROM Visits
LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.transaction_id IS NULL
GROUP BY Visits.customer_id;