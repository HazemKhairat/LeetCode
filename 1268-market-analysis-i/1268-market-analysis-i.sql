select u.user_id as buyer_id , u.join_date as join_date,  
count(case when o.order_date between '2019-01-01' and '2019-12-30' then o.order_date else null end)
as orders_in_2019 
from 
users u left join orders o on u.user_id = o.buyer_id
group by u.user_id, u.join_date