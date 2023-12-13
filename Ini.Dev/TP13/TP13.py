# =================================================================
#
# Code support du TP chaine d'entiers
# 
# Non redistribuable en dehors du Département Informatique de l'IUT
#
# =================================================================

from typing import Optional

# structure de maillon
class Maillon:
	data: int
	suivant: Optional["Maillon"]
	precedent: Optional["Maillon"]

# structure de liste
class ListeChainee:
	tete: Optional[Maillon]


def longueur(li: ListeChainee) -> int:
	courant : Maillon | None
	count : int
	
	courant = li.tete
	count = 0

	while courant:
		courant = courant.suivant
		count += 1
	return count

def last(li: ListeChainee) -> Maillon | None:
	current: Maillon | None

	current = li.tete
	if not current:
		return None

	while current.suivant:
		current = current.suivant

	return current

def afficheLC(li: ListeChainee) -> None:
	"""Fonction qui affiche les éléments de la liste.

	Dans cette version, chaque élément est affiché sur une ligne

	Args:
	----
		li (ListeChainee): la liste que l'on veut afficher
	"""
	print("1> ", end="")
	courant = li.tete
	while courant:
		print(courant.data, end=" -> ")
		courant = courant.suivant
	print("\b\b\b   ")

	print("2> ", end="")
	courant = last(li)
	while courant:
		print(courant.data, end=" -> ")
		courant = courant.precedent
	print("\b\b\b   ")


def ajoutQueue(li: ListeChainee, val: int):
	courant : Maillon | None
	new : Maillon | None

	courant = li.tete
	new = Maillon()
	new.data = val
	new.suivant = None
	new.precedent = None
	if not courant:
		li.tete = new
		return

	while courant.suivant:
		courant = courant.suivant
	if courant:
		new.precedent = courant
		courant.suivant = new

def ajoutTete(li: ListeChainee, val: int):
	new : Maillon | None

	new = Maillon()
	new.precedent = None

	new.data = val
	new.suivant = li.tete
	li.tete = new
	if new.suivant:
		new.suivant.precedent = new


def ajoutEnPos(li: ListeChainee, indice : int, val: int):
	courant : Maillon | None
	new : Maillon | None

	new = Maillon()

	new.data = val
	new.suivant = None
	new.precedent = None

	if indice == 0:
		ajoutTete(li, val)
	else:
		if li.tete:
			courant = li.tete
		else:
			exit(1)
		for i in range(indice - 1):
			if courant.suivant:
				courant = courant.suivant
		new.suivant = courant.suivant
		new.precedent = courant
		courant.suivant = new
		if new.suivant:
			new.suivant.precedent = new


def suppTete(li : ListeChainee):
	if not li.tete:
		return
	if not li.tete.suivant:
		li.tete = None
		return
	li.tete = li.tete.suivant
	li.tete.precedent = None


def suppQueue(li : ListeChainee):
	courant : Maillon | None

	courant = li.tete
	if not courant:
		return
	elif not courant.suivant:
		li.tete = None
		return

	while courant.suivant.suivant:
		courant = courant.suivant
	courant.suivant = None

def suppEnPos(li: ListeChainee, indice : int):
	courant : Maillon | None

	if indice == 0:
		suppTete(li)
	else:
		if li.tete:
			courant = li.tete
		else:
			exit(1)
		for i in range(indice - 1):
			if courant.suivant:
				courant = courant.suivant
		if courant.suivant:
			courant.suivant = courant.suivant.suivant
			if courant.suivant:
				courant.suivant.precedent = courant

def recherche(li: ListeChainee, val : int) -> int :
	courant : Maillon | None
	count : int

	count = 0
	courant = li.tete
	if not courant:
		return -1
	elif courant.data == val:
		return 0
	while courant.suivant:
		courant = courant.suivant
		count += 1
		if courant.data == val:
			return count
	else:
		return -1

if __name__=="__main__" :
	maLC = ListeChainee()
	maLC.tete = None

	afficheLC(maLC)
	assert longueur(maLC) == 0

	assert recherche(maLC, 8) == -1

	ajoutQueue(maLC, 5)

	afficheLC(maLC)
	assert longueur(maLC) == 1

	assert recherche(maLC, 5) == 0

	ajoutQueue(maLC, 6)

	afficheLC(maLC)
	assert longueur(maLC) == 2

	assert recherche(maLC, 5) == 0
	assert recherche(maLC, 6) == 1

	ajoutEnPos(maLC, 1, 7)

	afficheLC(maLC)
	assert longueur(maLC) == 3

	assert recherche(maLC, 7) == 1
	assert recherche(maLC, 2564) == -1

	ajoutTete(maLC, 4)

	afficheLC(maLC)
	assert longueur(maLC) == 4

	suppTete(maLC)

	afficheLC(maLC)
	assert longueur(maLC) == 3

	suppQueue(maLC)

	afficheLC(maLC)
	assert longueur(maLC) == 2

	suppEnPos(maLC, 1)

	afficheLC(maLC)
	assert longueur(maLC) == 1

	ajoutQueue(maLC, 7)
	ajoutQueue(maLC, 7)
	ajoutQueue(maLC, 7)
	suppEnPos(maLC, 1)

	afficheLC(maLC)
	assert longueur(maLC) == 3

	maLC = ListeChainee()
	maLC.tete = None

	suppTete(maLC)

	afficheLC(maLC)
	assert longueur(maLC) == 0

	suppQueue(maLC)

	afficheLC(maLC)
	assert longueur(maLC) == 0

	ajoutTete(maLC, 4)

	afficheLC(maLC)
	assert longueur(maLC) == 1

	suppTete(maLC)

	afficheLC(maLC)
	assert longueur(maLC) == 0

	ajoutTete(maLC, 4)

	afficheLC(maLC)
	assert longueur(maLC) == 1

	suppQueue(maLC)

	afficheLC(maLC)
	assert longueur(maLC) == 0