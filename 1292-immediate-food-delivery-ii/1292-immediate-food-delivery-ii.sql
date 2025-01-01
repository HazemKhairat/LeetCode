select round(
           count(delivery_id) * 100 / 
           (select count(distinct customer_id) 
            from Delivery), 2
       ) as immediate_percentage 
from Delivery
where (customer_id, order_date) in (
            select customer_id, min(order_date) 
            from Delivery 
            group by customer_id
       )
and order_date = customer_pref_delivery_date;