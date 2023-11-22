if __name__ == "__main__":
	num : int
	currChar : str
	prevChar : str
	string : str

	num = 0
	currChar = ""
	numStr = ""
	prevChar = ""
	string = ""
	isShit = False

	with open("lol.txt", "r") as f:
		while True:
			prevChar = currChar
			currChar = f.read(1)
			isShit = False
			if not currChar:
				break
			if currChar == "/" and num == 0:
				currChar = f.read(1)
				if currChar != "n" and not currChar.isdigit():
					print(f"/{currChar}", end='')
					continue
				while currChar.isdigit():
					num = num * 10 + int(currChar)
					numStr += currChar
					currChar = f.read(1)
				if currChar == "n":
					string += "\n"
					for i in range(num):
						print(string, end='')
					string = ""
					num = 0
					numStr = ""
					continue
				if currChar != "/":
					if numStr == "":
						print(f"/{currChar}{string}", end='')
					else:
						print(f"/{numStr}{currChar}{string}", end='')
					string = ""
					num = 0
					numStr = ""
					continue
				currChar = ""
				while currChar != "/":
					string += currChar
					currChar = f.read(1)
					if not currChar:
						print(f"/{numStr}/{string}", end='')
						isShit = True
						break
				if isShit:
					break
				for i in range(num):
					print(string, end='')
				num = 0
				string = ""
				numStr = ""
			else:
				print(currChar, end='')