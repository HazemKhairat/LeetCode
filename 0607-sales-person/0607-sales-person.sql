select name from SalesPerson s
where s.sales_id not in
(select sales_id from 
company c join Orders o 
on c.com_id = o.com_id
where c.name = 'RED')