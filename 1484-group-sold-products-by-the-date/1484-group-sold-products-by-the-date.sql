select sell_date, count(product) as 'num_sold', string_agg(product, ',') as products
from
(
    select distinct *
    from Activities
) t
group by sell_date