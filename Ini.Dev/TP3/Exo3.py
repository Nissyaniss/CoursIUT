if __name__ == "__main__":
# The code is checking if a given date is valid or not. It prompts the user to enter the number of
# days, months, and years. Then, it checks if the entered values are valid. If the date is valid, it
# prints "This date exists!". If the date is not valid, it prints "This date doesn't exist!" and exits
# the program.
	years		: int
	months		: int
	days		: int
	end			: int
	isLeapYear	: int

	years = 0
	months = 0
	days = 0
	end = 0
	isLeapYear = 0

	while end == 0:
		try:
			days = int(input("Enter number of days : "))
			if days > 0:
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
			months = int(input("Enter number of months : "))
			if months > 0:
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
			years = int(input("Enter number of years : "))
			if years > 0:
				end = 1
			else:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")

	if months > 12:
		print("This date doesn't exist !")
		exit(0)
	if days > 31:
		print("This date doesn't exist !")
		exit(0)
	if months == 4 or months == 6 or months == 9 or months == 11:
		if days > 30:
			print("This date doesn't exist !")
			exit(0)
	if (years % 4 == 0 and years % 100 > 0) or years % 400 == 0:
		isLeapYear = 1
	if months == 2:
		if isLeapYear == 1:
			if days > 29:
				print("This date doesn't exist !")
				exit(0)
		else:
			if days > 28:
				print("This date doesn't exist !")
				exit(0)
	print("This date exists !")