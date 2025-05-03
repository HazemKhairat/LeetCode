select product_id, product_name from Product
where (product_id, product_name) not in
(select p.product_id, p.product_name from 
product p left join sales s on p.product_id = s.product_id 
where s.sale_date not between '2019-01-01' and '2019-03-31' or s.sale_date is null)
