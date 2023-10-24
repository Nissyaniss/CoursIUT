# The code you provided is a Python program that takes user input for the number of days, months, and
# years and performs some calculations to increment the date by one day.
if __name__ == "__main__":

	day : int
	month : int
	year : int
	is_leap_year : bool
	end : int
	monthMaxDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	day = 0
	month = 0
	year = 0
	is_leap_year = False
	end = 0

	while end == 0:
		try:
			day = int(input("Enter number of days : "))
			if day > 0 and day <= 31:
				end = 1
			else:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	end = 0
	while end == 0:
		try:
			month = int(input("Enter number of months : "))
			if month > 0 and month <= 12:
				end = 1
			else:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	end = 0
	while end == 0:
		try:
			year = int(input("Enter number of years : "))
			if year > 0:
				end = 1
			else:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	
	day += 1
	if year // 4 and not (year // 100) or year // 400:
		is_leap_year = True
	if month == 2 and is_leap_year:
		monthMaxDays[1] = 28
	if month == 12 and day >= 31:
		day = 1
		month = 1
		year += 1
	if monthMaxDays[month - 1] < day:
		day = 1
		month += 1

	print(f"Your date i : {day} {month} {year}")
