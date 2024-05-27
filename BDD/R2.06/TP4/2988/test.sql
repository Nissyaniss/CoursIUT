select name,
sum(
	case
		when matches.team_1 = teams.id or matches.team_2 = teams.id
			then 1
		else 0
	end
) as matches,
sum(
	case
		when (matches.team_1 = teams.id and matches.team_1_goals > matches.team_2_goals)
			or (matches.team_2 = teams.id and matches.team_2_goals > matches.team_1_goals)
			then 1
		else 0
	end
) as victories,
sum(
	case
		when (matches.team_1 = teams.id and matches.team_1_goals < matches.team_2_goals)
			or (matches.team_2 = teams.id and matches.team_2_goals < matches.team_1_goals)
			then 1
		else 0
	end
) as defeats,
sum(
	case
		when (matches.team_1 = teams.id and matches.team_1_goals = matches.team_2_goals)
			or (matches.team_2 = teams.id and matches.team_2_goals = matches.team_1_goals)
			then 1
		else 0
	end
) as draws,
sum(
	case
		when (matches.team_1 = teams.id and matches.team_1_goals > matches.team_2_goals)
			or (matches.team_2 = teams.id and matches.team_2_goals > matches.team_1_goals)
			then 3
		when (matches.team_1 = teams.id and matches.team_1_goals = matches.team_2_goals)
			or (matches.team_2 = teams.id and matches.team_2_goals = matches.team_1_goals)
			then 1
		else 0
	end
) as score
from teams, matches
group by name
order by score desc, name
