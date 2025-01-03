select id, count(id) as num from 
(select requester_id as id from RequestAccepted
union all 
select accepter_id from RequestAccepted
) subquery
group by id
order by num desc
limit 1