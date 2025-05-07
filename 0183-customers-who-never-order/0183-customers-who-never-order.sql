select name as Customers from Customers where (name, id) not in
(select c.name, c.id from Customers c join Orders o on c.id = o.customerId)