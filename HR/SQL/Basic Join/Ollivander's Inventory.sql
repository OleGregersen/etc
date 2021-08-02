select w.id, p.age, w.coins_needed, w.power from wands as w join wands_property as p on w.code = p.code where p.is_evil = 0 and w.coins_needed = 
(select min(coins_needed) from wands as x join wands_property as y on x.code = y.code where x.power = w.power and y.age = p.age)
order by w.power desc, p.age desc;