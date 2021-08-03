select concat(name,'(',substr(occupation,1,1),')') as a from occupations order by a;
select concat('There are a total of ',count(occupation),' ',lower(occupation),'s.')
from occupations group by occupation order by count(occupation), occupation;
