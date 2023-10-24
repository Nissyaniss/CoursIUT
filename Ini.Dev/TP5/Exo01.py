def nb_parfait(nb : int) -> bool:
	i : int
	res : int

	i = 0
	res = 0

	for i in range(1, nb // 2 + 1):
		if not (nb % i):
			res = res + i
	return res == nb

if __name__ == "__main__":
	nb : int
	end : bool
	i : int

	nb = 0
	end = False
	i = 0

	while not end:
		try:
			nb = int(input("Enter n : "))
			if nb > 0:
				end = True
			else: 
				end = False
				print("Negative numbers not accepted!")
		except ValueError:
			end = False
			print("Not a number!")
	for i in range(1, nb + 1):
		if nb_parfait(i):
			print(f"{i} is perfect!")
		else:
			print(f"{i} is not perfect!")
