# The code you provided is a Python program that prompts the user to enter a number and then prints a
# pattern of asterisks based on that number.
if __name__ == "__main__":

	nb : int
	end : int
	i : int

	nb = 0
	end = 0
	i = 0

	while end == 0:
		try:
			nb = int(input("Enter number : "))
			if nb < 0:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
			else:
				end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")

	for i in range(1, nb * 2, 2):
		print(" " * (nb - i // 2) ,"*" * i)