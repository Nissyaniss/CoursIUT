(select FORMAT('Podium: %s',team) as name from league limit 3)
union all
(select format('Demoted: %s', team) as name from (select * from league order by position desc limit 2) as test order by position asc)
