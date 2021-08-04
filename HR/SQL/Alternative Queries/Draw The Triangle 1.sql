set @count := 21;
select repeat('* ', @count := @count - 1) from information_schema.tables limit 20;
