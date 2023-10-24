if __name__ == "__main__":
	isLeapYear : bool
	isGood : bool
	end : bool
	days : int
	months : int
	years : int

	isLeapYear = False
	isGood = True
	end = False
	days = 0
	months = 0
	years = 0

	while not end:
		try:
			days = int(input("Enter number of days :"))
			if days < 31 and days > 0:
				end = True
			else: 
				end = False
				print("Negative or numbers superior to 31 are not accepted!")
		except ValueError:
			end = False
			print("Not a number!")
	end = False
	while not end:
		try:
			months = int(input("Enter number of months :"))
			if months < 13 and months > 0:
				end = True
			else: 
				end = False
				print("Negative or numbers superior to 12 are not accepted!")
		except ValueError:
			end = False
			print("Not a number!")
	end = False
	while not end:
		try:
			years = int(input("Enter n :"))
			if years > 1583:
				end = True
			else: 
				end = False
				print("Negative or numbers inferior to 1583 are not accepted!")
		except ValueError:
			end = False
			print("Not a number!")


	isLeapYear = (not (years % 4) > 1 and (years % 100) != 0) or (not (years % 400))

	match months:
		case 1: isGood = days <= 31
		case 2: isGood = (isLeapYear and days <= 29) or (not (isLeapYear) and days <= 28)
		case 3: isGood = days <= 31
		case 4: isGood = days <= 30
		case 5: isGood = days <= 31
		case 6: isGood = days <= 30
		case 7: isGood = days <= 31
		case 8: isGood = days <= 31
		case 9: isGood = days <= 30
		case 10: isGood = days <= 31
		case 11: isGood = days <= 30
		case 12: isGood = days <= 31
		case _: isGood = False

	#G LE DROIT AU IF MTN
	if isGood:
		print("Your date is correct!")
	else:
		print("Your date is not correct!")

