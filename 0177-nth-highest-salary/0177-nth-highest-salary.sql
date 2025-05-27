create function getNthHighestSalary(n int) returns int
begin
    set n = n - 1;
    return (
        select distinct(salary) from employee
        order by salary desc
        limit n, 1
    );
end