from os import system
from re import I
from time import sleep

from more_itertools import iterate

class Auteur :
	lastName : str
	firstName : str
	nationality : str
	birthYear : int
	deathYear : int | None

class Livre :
	title : str
	author : Auteur
	year : int
	pages : int

def checkInputInt(message : str, bornInf : int | None, bornSup : int | None, isNone : bool) -> int | None:
	end : bool
	res : int
	inputRes : str

	end = False
	res = 0

	if bornInf is not None and bornSup is not None:
		while end == False:
			inputRes = input(message)
			if isNone and inputRes == "":
				return None
			try:
				res = int(inputRes)
				if res >= bornInf and res <= bornSup:
					end = True
				else:
					print("Value Error")
			except ValueError:
				print("Value Error")
	elif bornInf is not None and bornSup is None:
		while end == False:
			inputRes = input(message)
			if isNone and inputRes == "":
				return None
			try:
				res = int(inputRes)
				if res >= bornInf:
					end = True
				else:
					print("Value Error")
			except ValueError:
				print("Value Error")
	else:
		while end == False:
			inputRes = input(message)
			if isNone and inputRes == "":
				return None
			try:
				res = int(inputRes)
				end = True
			except ValueError:
				print("Value Error")
	return res

def DisplayMenu(error : bool):
	system("clear")
	if error:
		print("Value Error")
	print("1 - Afficher l'ensemble des livres de la bibliothèque")
	print("2 - Ajouter un nouveau livre")
	print("3 - Rechercher un livre (par le titre)")
	print("4 - Ajouter un auteur")
	print("5 - Quitter")
	print("Votre choix : ", end='')

def ShowBookList(bookList : list[Livre]):
	system("clear")
	if len(bookList) == 0:
		print("Liste vide")
		return

	for e in bookList:
		if e.author.deathYear is None:
			print(f"{e.title}({e.pages} pages) sortie en {e.year} par {e.author.lastName} {e.author.firstName} ({e.author.birthYear} - Aujourd'hui) de nationalité {e.author.nationality}")
		else:
			print(f"{e.title}({e.pages} pages) sortie en {e.year} par {e.author.lastName} {e.author.firstName} ({e.author.birthYear} - {e.author.deathYear})de nationalité {e.author.nationality}.")

def SearchTitle(bookList : list[Livre], title : str):
	for e in bookList:
		if e.title == title:
			print(f"{e.title}({e.pages} pages) par {e.author} sortie en {e.year}")
			break
	input("Press Enter to continue")

def isAuthor(name : str, authorList : list[Auteur]) -> tuple[bool, int]:
	for i, e in enumerate(authorList):
		if e.lastName == name:
			return  (True, i)
	i = -1
	return (False, i)

def addAuthor(authorList : list[Auteur]) -> Auteur:
	author : Auteur
	fuckPylance : int | None

	system("clear")
	author = Auteur()
	author.lastName = input("Quel est le nom ? : ")
	author.firstName = input("Quel est le prénom ? : ")
	author.nationality = input("Quelle est la nationalité ? : ")
	fuckPylance = checkInputInt("Quelle est l'année de naissance ? : ", None, None, False)
	if fuckPylance is None:
		author.birthYear = 0
	else:
		author.birthYear = fuckPylance
	author.deathYear = checkInputInt("Quelle est l'année de décès ? : ", author.birthYear, None, True)
	authorList.append(author)
	return author

def AddBook(bookList : list[Livre], authorList : list[Auteur]):
	book : Livre
	fuckPylance : int | None

	system("clear")
	while True:
		book = Livre()
		book.title = input("Quel est le titre ? : ")
		isAuthorTuple = isAuthor(input("Qui est l'auteur ? : "), authorList)
		if isAuthorTuple[0]:
			book.author = authorList[isAuthorTuple[1]]
		else:
			print("L'auteur n'existe pas, alors vous devez en créer un.")
			sleep(1)
			book.author = addAuthor(authorList)
		fuckPylance = checkInputInt("Quelles est l'année de parution ? : ", book.author.birthYear, None, False)
		if fuckPylance is None:
			book.year = 0
		else:
			book.year = fuckPylance
		fuckPylance = checkInputInt("Combien de pages ? : ", 1, None, False)
		if fuckPylance is None:
			book.pages = 0
		else:
			book.pages = fuckPylance
		bookList.append(book)
		if input("Voulez vous arrêter d'enregistrer des livres ? [y/N] : ") == "y":
			continue
		else:
			break

if __name__ == "__main__":
	bookList : list[Livre]
	authorList : list[Auteur]
	author : Auteur
	book : Livre
	choice : int
	fuckPylance : int | None

	bookList = []
	authorList = []
	author = Auteur()
	book = Livre()
	choice = 0

	while True:
		DisplayMenu(False)
		fuckPylance = checkInputInt("", 1, 5, False)
		if fuckPylance is None:
			choice = 0
		else:
			choice = fuckPylance
		if choice == 1:
			ShowBookList(bookList)
			input("Press Enter to continue")
		elif choice == 2:
			AddBook(bookList, authorList)
		elif choice == 3:
			system("clear")
			SearchTitle(bookList, input("Quel Livre cherchez vous (Par titre) ? :"))
		elif choice == 4:
			system("clear")
			addAuthor(authorList)
		elif choice == 5:
			break