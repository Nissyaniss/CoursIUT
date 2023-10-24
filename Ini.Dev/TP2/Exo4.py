import os
import colorama

def correctNumber(numberToEnter : str, error : str) -> int :
	nb	: int
	end	: int

	end = 0
	nb = 0

	while end == 0:
		try:
			nb = int(input("Enter number of " + numberToEnter + " : "))
			if nb >= 0:
				end = 1
			else:
				print(colorama.Fore.RED + error + colorama.Fore.WHITE)
				os.system("clear||cls")
		except ValueError:
			os.system("clear||cls")
			print(colorama.Fore.RED + error + colorama.Fore.WHITE)
	return nb

def menu():
	print("Menu\n\n")
	print("Choose what you want to do :\n")
	print("\t1- Convert seconds into seconds/minutes/hours/days/month/year")
	print("\t2- Convert seconds/minutes/hours/days/month/year into seconds\n")

if __name__ == "__main__":
	seconds	: int
	minutes	: int
	hours	: int
	days	: int
	weeks	: int
	month	: int
	year	: int
	choice	: int
	end		: int

	seconds = 0
	minutes = 0
	hours = 0
	days = 0
	weeks = 0
	month = 0
	year = 0
	choice = 0
	end = 0

	menu()
	while end == 0:
		try:
			choice = int(input("Choose the number : "))
			if choice >= 1 and choice <= 2:
				end = 1
			else:
				os.system("clear||cls")
				print(colorama.Fore.RED + "ERROR : Incorrect Value, accepted value are [1], [2]" + colorama.Fore.WHITE)
				menu()
		except ValueError:
			os.system("clear||cls")
			print(colorama.Fore.RED + "ERROR : Incorrect Value, accepted value are [1], [2]" + colorama.Fore.WHITE)
			menu()
	if choice == 1:
		end = 0
		seconds = correctNumber("seconds", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		year = seconds // 31536000
		seconds = seconds % 3156000
		month = seconds // 2678400
		seconds = seconds % 2678400
		month = seconds // 604800
		seconds = seconds % 604800
		days = seconds // 86400
		seconds = seconds % 86400
		hours = seconds // 3600
		seconds = seconds % 3600
		minutes = seconds // 60
		seconds = seconds % 60
		print(f"Your time is {year}/{month}/{weeks}/{days} {hours}:{minutes}:{seconds}")
	if choice == 2:
		year = correctNumber("years", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		month = correctNumber("month", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		weeks = correctNumber("weeks", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		days = correctNumber("days", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		hours = correctNumber("hours", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		minutes = correctNumber("minutes", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		seconds = correctNumber("seconds", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)

		seconds =+ (year * 31536000) + (month * 3156000) + (weeks * 604800) + (days * 86400) + (hours * 3600) + (minutes * 60)
		print(f"Result is {seconds} seconds.")