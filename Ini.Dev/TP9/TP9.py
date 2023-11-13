from os import system
from time import sleep

class Livre :
	title : str
	author : str
	year : int
	pages : int

def DisplayMenu(error : bool):
	system("clear")
	if error:
		print("Value Error")
	print("1 - Afficher l'ensemble des livres de la bibliothèque")
	print("2 - Ajouter un nouveau livre")
	print("3 - Rechercher un livre (par le titre)")
	print("4 - Quitter")
	print("Votre choix : ", end='')

def ShowBookList(bookList : list[Livre]):
	system("clear")
	if len(bookList) == 0:
		print("Liste vide")
		return

	for e in bookList:
		print(f"{e.title}({e.pages} pages) par {e.author} sortie en {e.year}")

def SearchTitle(bookList : list[Livre], title : str):
	for e in bookList:
		if e.title == title:
			print(f"{e.title}({e.pages} pages) par {e.author} sortie en {e.year}")
			break
	input("Press Enter to continue")

def AddBook(bookList : list[Livre]):
	end : bool
	book : Livre

	end = False

	system("clear")
	while True:
		book = Livre()
		book.title = input("Quel est le titre ? : ")
		book.author = input("Qui est l'auteur ? : ")
		while end == False:
			try:
				book.year = int(input("Quelles est l'année de parution ? : "))
				end = True
			except ValueError:
				print("Value Error")
				sleep(1)
				system("clear")
		end = False
		while end == False:
			try:
				book.pages = int(input("Combien de pages ? : "))
				end = True
			except ValueError:
				print("Value Error")
				sleep(1)
				system("clear")
		end = False
		bookList.append(book)
		if input("Voulez vous arrêter d'enregistrer des livres ? [y/N] : ") == "y":
			continue
		else:
			break

if __name__ == "__main__":
	bookList : list[Livre]
	book : Livre
	end : bool
	choice : int

	bookList = []
	book = Livre()
	end = False
	choice = 0

	while True:
		DisplayMenu(False)
		while end == False:
			try:
				choice = int(input())
				end = True
				if choice <= 0 or choice > 5:
					end = False
					DisplayMenu(True)
			except ValueError:
				end = False
				DisplayMenu(True)
		end = False
		if choice == 1:
			ShowBookList(bookList)
			input("Press Enter to continue")
		elif choice == 2:
			AddBook(bookList)
		elif choice == 3:
			system("clear")
			SearchTitle(bookList, input("Quel Livre cherchez vous (Par titre) ? :"))
		elif choice == 4:
			break