select firstName , lastName , city, state
from person p left join address a
on p.personId = a.personId