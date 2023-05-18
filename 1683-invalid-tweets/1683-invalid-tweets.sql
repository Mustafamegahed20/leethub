/* Write your T-SQL query statement below */
select tweet_id 
from tweets 
where LEN(content)>15