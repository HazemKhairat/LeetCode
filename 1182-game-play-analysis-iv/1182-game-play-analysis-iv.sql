select 
    round(count(a1.player_id) / (select count(distinct a3.player_id) from Activity a3), 2) as fraction
from 
    Activity a1
where (a1.player_id, DATE_SUB(a1.event_date, interval 1 day)) in(
select 
    a2.player_id,
    min(a2.event_date) 
from 
    Activity a2
group by a2.player_id
)