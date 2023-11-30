#!/usr/bin/env python3
from __future__ import annotations

class List:
	tete: Node


class Node:
	valeur: int
	suivant: Node
	precedent: Node


# ================ Compiler generated code, please don't edit ================
class UninitMeta(type):
	def __instancecheck__(cls: UninitMeta, instance: object) -> bool:
		return True


UninitClass = UninitMeta("UninitClass", (), {})
Uninit = UninitClass()
# ============================================================================


def ajouter(liste: List, nbr: int) -> None:
	nouveau: Node = Uninit

	nouveau = Node()
	nouveau.valeur = nbr
	nouveau.suivant = Uninit
	nouveau.precedent = Uninit
	if liste.tete != Uninit:
		liste.tete.precedent = nouveau
		nouveau.suivant = liste.tete


def supprimerTete(liste: List) -> None:
	save: Node = Uninit

	save = Node()
	if liste.tete != Uninit:
		save = liste.tete
		liste.tete = liste.tete.suivant
		liste.tete.suivant = Uninit


def supprimerQueue(liste: List) -> None:
	current: Node = Uninit
	save: Node = Uninit

	if liste.tete != Uninit:
		save = Node()
		current = liste.tete
		while current.suivant != Uninit:
			current = current.suivant
		save = current
		current = current.precedent
		current.precedent = Uninit
