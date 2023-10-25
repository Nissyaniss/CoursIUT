def part1():
	liste : list[int]

	liste = [1, 2, 3, 4, 5]
	print(liste)

def part2():
	liste : list[list[int]]

	liste = []
	for i in range(0, 3):
		liste.append([int(input(f"Liste {i} : ")), int(input(f"List {i} : ")), int(input(f"Liste {i} : "))])
	print(liste)

def part3():
	listeStr : list[str]

	listeStr = input("Entrez une liste d'entiers : ").split()
	print(part3bis(listeStr))


def part3bis(liste : list[str]) -> list[int]:
	listeInt : list[int]

	listeInt = []
	for i in liste:
		listeInt.append(int(i))
	return listeInt

if __name__ == "__main__":
	part1()
	part2()
	part3()
