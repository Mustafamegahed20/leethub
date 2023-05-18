/* Write your T-SQL query statement below */
select distinct id 
from (select author_id as id ,viewer_id
from views 
where author_id =viewer_id)t

order by id asc
