if __name__ == "__main__":
	end : bool
	nb : int

	end = False
	nb = 0

	while not end:
		try:
			nb = int(input("Enter nb :"))
			if nb > 0:
				end = True
			else: 
				end = False
				print("Negative numbers are not accepted!")
		except ValueError:
			end = False
			print("Not a number!")
	
	for i in range(1, nb + 1):
		for y in range(1, i + 1):
			print(f"{y} ", end="")
		print("")

