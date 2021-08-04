set @count := 0;
select repeat('* ', @count := @count + 1) from information_schema.tables limit 20;