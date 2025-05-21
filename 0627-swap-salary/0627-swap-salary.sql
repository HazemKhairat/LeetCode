# Write your MySQL queryupdate Salary 
update salary
set sex =
case 
when sex = 'm' then 'f'
when sex = 'f' then 'm'
end 
