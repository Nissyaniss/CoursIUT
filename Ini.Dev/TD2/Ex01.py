if __name__ == '__main__':
	tempstr	: str
	tempint	: int
	i		: int
	numbers : list[int]

	i		= 0
	numbers = [0, 0, 0]
	tempstr = ""
	while tempstr == "":
		tempstr = input("Entrer number1 : ")
		if tempstr.isnumeric():
			numbers[0] = int(tempstr)
		else:
			print("Invalid Number !")
			tempstr = ""

	tempstr = ""
	while tempstr == "":
		tempstr = input("Entrer number2 : ")
		if tempstr.isnumeric():
			numbers[1] = int(tempstr)
		else:
			print("Invalid Number !")
			tempstr = ""

	tempstr = ""
	while tempstr == "":
		tempstr = input("Entrer number3 : ")
		if tempstr.isnumeric():
			numbers[2] = int(tempstr)
		else:
			print("Invalid Number !")
			tempstr = ""

	while i < 2:
		if numbers[i] > numbers[i + 1]:
			tempint = numbers[i]
			numbers[i] = numbers[i + 1]
			numbers[i + 1] = tempint
		i = i + 1
	i = 0
	while i < 2:
		if numbers[i] > numbers[i + 1]:
			tempint = numbers[i]
			numbers[i] = numbers[i + 1]
			numbers[i + 1] = tempint
		i = i + 1

	if numbers[0] == numbers[1] and numbers[1] == numbers[2]:
		print(f"{numbers[0]} = {numbers[1]} = {numbers[2]}")
	else :
		if numbers[0] == numbers[1]:
			print(f"{numbers[0]} = {numbers[1]} < {numbers[2]}")
		else:
			if numbers[1] == numbers[2]:
				print(f"{numbers[0]} < {numbers[1]} = {numbers[2]}")
			else:
				print(f"{numbers[0]} < {numbers[1]} < {numbers[2]}")
