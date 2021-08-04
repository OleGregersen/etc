select round(lat_n, 4) from 
(select lat_n, row_number() over (order by lat_n) as rown from station) as x 
where rown = (select round((count(lat_n) + 1) / 2, 0) from station)