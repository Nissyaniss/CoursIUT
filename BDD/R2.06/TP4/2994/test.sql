select doctors.name, sum(round(((attendances.hours*150)*(work_shifts.bonus/100.0+1)),1))
	as salary from doctors, work_shifts, attendances
	where
	attendances.id_doctor=doctors.id and
	attendances.id_work_shift=work_shifts.id
	group by doctors.name
	order by salary desc
