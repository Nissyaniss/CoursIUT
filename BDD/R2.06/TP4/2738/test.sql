select name, round((math*2 + specific*3 + project_plan*5) / 10, 2) as avg from candidate, score where
candidate.id = score.candidate_id
order by avg desc
