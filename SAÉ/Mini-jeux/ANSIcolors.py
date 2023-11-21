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
	return '\x1b[38:5:11m' + string + '\x1b[m'