select n, if(p is null, 'Root', if((select count(*) from bst where p=a.n)>0, 'Inner', 'Leaf'))
from bst as a order by n;