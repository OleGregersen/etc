set @prime := 1; set @div := 1;
select group_concat(prime separator '&') from (select @prime := @prime + 1 as prime 
from information_schema.tables t1, information_schema.tables t2 limit 1000) prime 
where not exists (select * from (select @div := @div + 1 as divisor from information_schema.tables t3, information_schema.tables t4 limit 1000) divisors 
where mod(prime, divisor) = 0 and prime <> divisor);