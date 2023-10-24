def checkAge(age : int, borneUp : int, borneDown: int, message : str, list : list[str]):
	if age >= borneDown and age < borneUp:
		list.append(message)

if __name__ == "__main__":
	date1Days		: int
	date1Months		: int
	date1Years		: int
	date2Days		: int
	date2Months		: int
	date2Years		: int
	age				: int
	criteria		: list[str]

date1Days = int(input("Enter day of date 1 : "))
date1Months = int(input("Enter month of date 1 : "))
date1Years = int(input("Enter year of date 1 : "))
date2Days = int(input("Enter day of date 2 : "))
date2Months = int(input("Enter month of date 2 : "))
date2Years = int(input("Enter year of date 2 : "))

if date1Years > date2Years:
	print("Date 1 superior to date 2")
elif date1Years == date2Years:
	if date1Months > date2Months:
		print("Date 1 superior to date 2")
	elif date1Months == date2Months:
		if date1Days > date2Days:
			print("Date 1 superior to date 2")
if date2Days == date1Days and date1Years == date2Years and date1Months == date2Months:
	print("Your just born dont go on a computer already !")

age = date2Years - date1Years
if date1Months > date2Months:
	age -= 1
elif (date1Months == date2Months) and (date1Days > date2Days):
	age -= 1

criteria = []
if age < 18:
	criteria.append("mineur")
elif age >= 18:
	criteria.append("majeur")
	checkAge(age, 30, 20, "vingtenaire", criteria)
	checkAge(age, 40, 30, "trentenaire", criteria)
	checkAge(age, 50, 40, "quadragénaire", criteria)
	checkAge(age, 60, 50, "quinquagénaire", criteria)
	checkAge(age, 70, 60, "sexagénaire", criteria)
	if age >= 65:
		criteria.append("retraitée")

for e in criteria:
	print(e)