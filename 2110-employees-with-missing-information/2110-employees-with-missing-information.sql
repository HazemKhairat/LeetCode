select employee_id from

(select employee_id from Employees 
where employee_id not in
(select e.employee_id from Employees e join Salaries s on e.employee_id = s.employee_id)

union

select employee_id from Salaries where employee_id not in
(select e.employee_id from Employees e join Salaries s on e.employee_id = s.employee_id)) as subquery

order by employee_id