select distinct logs1.num as ConsecutiveNums 
from Logs logs1, Logs logs2, Logs logs3
where 
    logs3.id - 2 = (logs2.id - 1)
    and (logs2.id - 1) = logs1.id
    and logs1.num = logs2.num
    and logs2.num = logs3.num