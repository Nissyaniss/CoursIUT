def fibonnaci(nb : int) -> int:
	"""
	The function calculates the nth Fibonacci number recursively.
	
	:param nb: The parameter "nb" represents the position of the Fibonacci number that you want to
	calculate. For example, if nb = 5, it means you want to calculate the 5th Fibonacci number
	:type nb: int
	:return: the nth Fibonacci number.
	"""

	if nb == 0:
		return 0
	elif nb == 1:
		return 1
	else:
		return (fibonnaci(nb - 1) + fibonnaci(nb - 2))

if __name__ == "__main__":

# The code block you provided is asking the user to enter an upper bound value (`upper_bound`) and
# then using a while loop to calculate and print the Fibonacci numbers (`result`) until the Fibonacci
# number is greater than the upper bound.
	upper_bound : int
	end : int
	i : int
	result : int

	end = 0
	upper_bound = 0
	i = 0
	result = 0

	while end == 0:
		try:
			upper_bound = int(input("Enter borne_sup : "))
			if upper_bound < 0:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
			else:
				end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	while (result := fibonnaci(i)) < upper_bound:
		print("Value U", i, " is ", result, sep="")
		i += 1