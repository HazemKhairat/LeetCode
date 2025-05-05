select Email from Person 
group by email
having count(email) >= 2