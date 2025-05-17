select employee_id,
(case when 
(employee_id mod 2) = 1 and name not like 'M%' 
then salary 
else 0 end) as bonus 
from employees
order by employee_id
