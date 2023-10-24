def ft_gcd(nb1 : int, nb2 : int) -> int:
	"""
	The function `ft_gcd` calculates the greatest common divisor (GCD) of two numbers using the
	Euclidean algorithm.
	
	:param nb1: The first number for which you want to find the greatest common divisor
	:type nb1: int
	:param nb2: The parameter nb2 represents the second number for which we want to find the greatest
	common divisor (GCD)
	:type nb2: int
	:return: The function `ft_gcd` returns the greatest common divisor (GCD) of `nb1` and `nb2`.
	"""
	if nb1 != 0 and nb2 != 0:
		nb1 = nb1 % nb2
		nb1 = ft_gcd(nb2, nb1)

	return nb1

if __name__ == "__main__":
# The code block you provided is declaring and initializing several variables (`nb1`, `nb2`, `gdc`,
# `end`, `tmp`) and then using them to prompt the user for two numbers (`nb1` and `nb2`).
	nb1	: int
	nb2	: int
	gdc	: int
	end	: int
	tmp	: int

	nb1 = 0
	nb2 = 0
	gdc = 0
	end = 0
	tmp = 0

	while end == 0:
		try:
			nb1 = int(input("Enter number 1 : "))
			end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	end = 0
	while end == 0:
		try:
			nb2 = int(input("Enter number 2 : "))
			end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")

	if nb1 == nb2:
		result = nb1

	result = ft_gcd(nb1, nb2)
	print(f"The result is {result}")
