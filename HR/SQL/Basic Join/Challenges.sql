select h.hacker_id, h.name, count(c.challenge_id) as total_count
from hackers h join challenges c on h.hacker_id = c.hacker_id
group by h.hacker_id, h.name having total_count = 
(select count(temp1.challenge_id) as max_count from challenges temp1
group by temp1.hacker_id order by max_count desc limit 1)
or total_count in
(select distinct other_counts from 
(select h2.hacker_id, h2.name, count(c2.challenge_id) as other_counts
from hackers h2 join challenges c2 on h2.hacker_id = c2.hacker_id group by h2.hacker_id, h2.name) temp2 group by other_counts having count(other_counts) =1)
order by total_count desc, h.hacker_id