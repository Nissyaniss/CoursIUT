# The code you provided is a simple calculator program in Python. It allows the user to enter two
# numbers and an arithmetic operation (+, -, *, /). The program then performs the operation on the two
# numbers and displays the result.
if __name__ == "__main__":
	nb1		: float
	nb2		: float
	result	: float
	end		: int
	sign	: str

	nb1 = 0
	nb2 = 0
	result = 0
	end = 0
	sign = ""

	while end == 0:
		try:
			nb1 = float(input("Enter number 1 : "))
			end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	end = 0
	while end == 0:
		try:
			nb2 = float(input("Enter number 2 : "))
			end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	end = 0
	while end == 0:
		sign = input("Enter sign : ")
		if sign == "*" or sign == "/" or sign == "+" or sign == "-":
			end = 1
		else:
			print("ERROR[ValueError] : Value aceppet : [+], [-], [*], [/]")
			end = 0

	if sign == "*":
		result = nb1 * nb2
	elif sign == "/":
		result = nb1 / nb2
	elif sign == "+":
		result = nb1 + nb2
	elif sign == "-":
		result = nb1 - nb2

	print(f"The result of {nb1} {sign} {nb2} is {result}")