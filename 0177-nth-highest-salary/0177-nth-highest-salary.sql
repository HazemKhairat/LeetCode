CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    declare x INT;
    set x = N - 1;
  RETURN (
    select distinct(salary) from Employee 
    order by salary desc
    limit 1 
    OFFSET x
  );
END