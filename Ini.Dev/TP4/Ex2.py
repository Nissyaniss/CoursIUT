def is_prime(nb : int) -> bool:
	"""
	The function `is_prime` checks if a given number is prime or not and returns a boolean value.
	
	:param nb: The parameter `nb` is an integer that represents the number we want to check if it is
	prime or not
	:type nb: int
	:return: The function `is_prime` returns a boolean value. It returns `True` if the input number
	(`nb`) is a prime number, and `False` otherwise.
	"""

	i : int

	i = 2

	if nb <= 1:
		return False
	while i < nb:
		if (not (nb % i)):
			return False
		i += 1
	return True
	
if __name__ == "__main__":

# The code is asking the user to enter a number and then checks if the entered number is prime or not
# using the `is_prime` function.
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
	if is_prime(nb):
		print(nb, "est premier")
	else:
		print(nb, "n'est pas premier")