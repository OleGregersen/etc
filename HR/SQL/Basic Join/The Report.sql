select case when g.grade > 7 then s.name else null end as names, g.grade, s.marks
from students s join grades g on s.marks between g.min_mark and g.max_mark
order by g.grade desc, names asc, s.marks asc;