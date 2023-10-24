if __name__ == "__main__":
# The code you provided is a Python program that compares two numbers entered by the user.
	number1	: float
	number2	: float
	end		: int

	number1 = 0
	number2 = 0
	end = 0

	while end == 0:
		try:
			number1 = int(input("Enter number1 :\n"))
			end = 1
		except ValueError:
			print("Error : Invalid Value")
	end = 0
	while end == 0:
		try:
			number2 = int(input("Enter number2 :\n"))
			end = 1
		except ValueError:
			print("Error : Invalid Value")

	if number1 < number2:
		print(f"{number1} < {number2}")
	elif number1 > number2:
		print(f"{number1} > {number2}")
	elif number1 == number2:
		print(f"{number1} = {number2}")