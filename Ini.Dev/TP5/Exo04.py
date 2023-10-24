if __name__ == "__main__":
	end : bool
	nb : int
	lines : int
	cols : int
	i : int
	loops : int
	is2Part : bool
	spaces : int

	end = False
	nb = 1000
	lines = 0
	cols = 0
	loops = 0
	i = 0
	is2Part = False

	while not end:
		try:
			nb = int(input("Enter nb : "))
			if nb > 0:
				end = True
			else: 
				end = False
				print("Negative numbers are not accepted!")
		except ValueError:
			end = False
			print("Not a number!")

	spaces = len(str(nb * 2)) + 1

	i = nb * 2
	while loops != nb * 2 + 1:
		while cols != nb * 2 + 1:
			if cols < nb:
				print(" " * (len(str(nb * 2)) - len(str(i - lines)) - cols) + f"{i - lines}" + " " * (spaces - len(str(i - 1 - lines))), end='')
				i = i - 1
			elif cols == nb:
				print(f"{nb - lines}" + " " * (spaces - len(str(nb + 1 - lines))), end='')
				i = nb + 1
			elif cols <= nb * 2 + 1:
				print(f"{i - lines}" + " " * (spaces - len(str(i + 1 - lines))) , end='')
				i = i + 1
			cols = cols + 1
		print("")
		if lines == nb and not is2Part:
			lines = nb - 1
			is2Part = True
		elif is2Part:
			lines = lines - 1
		else:
			lines = lines + 1
		i = nb * 2
		loops = loops + 1
		cols = 0









