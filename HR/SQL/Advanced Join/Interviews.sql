select c.contest_id, c.hacker_id, c.name, 
sum(sg.total_submissions), sum(sg.total_accepted_submissions), 
sum(vg.total_views), sum(vg.total_unique_views) from contests as c
join colleges as col on c.contest_id = col.contest_id
join challenges as cha on cha.college_id = col.college_id left join
(select ss.challenge_id, sum(ss.total_submissions) as total_submissions, sum(ss.total_accepted_submissions) as total_accepted_submissions from submission_stats as ss 
group by ss.challenge_id) as sg
on cha.challenge_id = sg.challenge_id left join
(select vs.challenge_id, sum(vs.total_views) as total_views, 
sum(vs.total_unique_views) as total_unique_views
from view_stats as vs group by vs.challenge_id) as vg on cha.challenge_id = vg.challenge_id
group by c.contest_id, c.hacker_id, c.name having sum(sg.total_submissions) +
sum(sg.total_accepted_submissions) + sum(vg.total_views) + sum(vg.total_unique_views) > 0
order by c.contest_id;
