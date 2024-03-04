def inverseColor(string : str) -> str:
	"""
	Inverse la couleur du string avec un code ANSI

	Entrée : string : str
	Symbolise le string a modifié

	Sortie : str
	Symbolise le string formaté
	"""
	return '\x1b[7m' + string + '\x1b[m'

def stringRed(string : str) -> str:
	"""
	Change la couleur en rouge du string avec un code ANSI

	Entrée : string : str
	Symbolise le string a modifié

	Sortie : str
	Symbolise le string formaté
	"""
	return '\x1b[31m' + string + '\x1b[m'

def stringYellow(string : str) -> str:
	"""
	Change la couleur en rouge du string avec un code ANSI

	Entrée : string : str
	Symbolise le string a modifié

	Sortie : str
	Symbolise le string formaté
	"""
	return '\x1b[93m' + string + '\x1b[m'

def backStringRed(string : str) -> str:
	"""
	Change la couleur du background du string en rouge avec un code ANSI

	Entrée : string : str
	Symbolise le string a modifié

	Sortie : str
	Symbolise le string formaté
	"""
	return '\x1b[41m' + string + '\x1b[m'

def backStringYellow(string : str) -> str:
	"""
	Change la couleur du background du string en jaune avec un code ANSI

	Entrée : string : str
	Symbolise le string a modifié

	Sortie : str
	Symbolise le string formaté
	"""
	return '\x1b[103m' + string + '\x1b[m'

def stripANSIColors(string : str) -> str:
	"""
	Enlève les couleurs ANSI d'une chaîne de caractères

	Entrée : string : str
	string symbolise la chaîne de caractères ou l'on veux enlever les couleurs
	"""
	result : str
	i : int
	j : int

	result = ""
	i = 0
	j = 0

	while i < len(string):
		if string[i] == '\x1B':
			j = i
			while string[j] != 'm':
				j += 1
			i = j + 1
		else:
			result += string[i]
			i += 1
	return result