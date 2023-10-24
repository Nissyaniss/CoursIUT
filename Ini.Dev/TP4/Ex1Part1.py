def fibonnaci(nb : int) -> int:
	"""
	The function calculates the Fibonacci number at a given index using recursion.
	
	:param nb: The parameter "nb" represents the position of the Fibonacci number that you want to
	calculate
	:type nb: int
	:return: the nth Fibonacci number, where n is the input parameter nb.
	"""
	if nb == 0:
		return 0
	elif nb == 1:
		return 1
	else:
		return (fibonnaci(nb - 1) + fibonnaci(nb - 2))

if __name__ == "__main__":

# The code block you provided is responsible for taking user input, validating it, and then printing
# the Fibonacci sequence up to the entered number.
	nb : int
	end : int

	end = 0
	nb = 0

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
	for i in range(0, nb + 1):
		print("Value U", i, " is ", fibonnaci(i), sep="")
