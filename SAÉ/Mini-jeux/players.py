import json

from termUtils import printAt

def isPlayerExisting(player: str) -> bool:
	"""
	Vérifie si un joueur existe

	Entrée : player : str
	player symbolise le nom du joueur

	Sortie : bool
	True si le joueur existe, False sinon
	"""
	data: dict[str, tuple[int, int, int, int]] # Déclaration du dictionnaire

	with open("players.json", "r") as jsonFile: # Récupère les données du fichier
		data = json.load(jsonFile)

	if player in data: # Vérifie si le joueur existe
		return True
	else:
		return False

def addPlayer(player: str) -> None:
	"""
	Ajoute un joueur

	Entrée : player : str
	player symbolise le nom du joueur
	"""
	data: dict[str, tuple[int, int, int, int]] # Déclaration du dictionnaire

	with open("players.json", "r") as jsonFile: # Récupère les données du fichier
		data = json.load(jsonFile)

	data.update({player : (0, 0, 0, 0)}) # Ajoute le joueur

	with open("players.json", "w") as outputFile: # Écrit les données dans le fichier
		json.dump(data, outputFile, sort_keys=True, indent='\t', separators=(',', ': '))

def addPoint(player: str, game: int) -> None:
	"""
	Ajoute un point à un joueur

	Entrée : player : str
	player symbolise le nom du joueur

	Entrée : game : int
	game symbolise le jeu
	"""
	data: dict[str, tuple[int, int, int, int]] # Déclaration du dictionnaire

	with open("players.json", "r") as jsonFile: # Récupère les données du fichier
		data = json.load(jsonFile)

	playerData = data[player] # Récupère les données du joueur
	if game == 1:
		playerData = (playerData[0] + 1, playerData[1],
					  playerData[2], playerData[3]) # Ajoute un point au joueur
	elif game == 2:
		playerData = (playerData[0], playerData[1] +
					  1, playerData[2], playerData[3])
	elif game == 3:
		playerData = (playerData[0], playerData[1],
					  playerData[2] + 1, playerData[3])
	else:
		playerData = (playerData[0], playerData[1],
					  playerData[2], playerData[3] + 1)

	data[player] = playerData # Ajoute les données du joueur
	with open("players.json", "w") as outputFile: # Écrit les données dans le fichier
		json.dump(data, outputFile, sort_keys=True, indent='\t', separators=(',', ': '))

def printScoreboard(player1: str, player2: str) -> None:
	"""
	Affiche le tableau des scores

	Entrée : player1 : str
	player1 symbolise le nom du joueur 1

	Entrée : player2 : str
	player2 symbolise le nom du joueur 2
	"""
	data: dict[str, tuple[int, int, int, int]] # Déclaration du dictionnaire
	playerFormat : str

	with open("players.json", "r") as jsonFile: # Récupère les données du fichier
		data = json.load(jsonFile)

	if len(player1) > 10: # Formate le nom des joueurs si ils sont trop longs
		playerFormat = player1[:10] + "..."
	else:
		playerFormat = player1
	printAt(6, 5, f"{playerFormat} :") # Affiche le tableau des scores
	printAt(7, 6, f"Devinette   = {data[player1][0]}")
	printAt(8, 6, f"Allumette   = {data[player1][1]}")
	printAt(9, 6, f"Morpion     = {data[player1][2]}")
	printAt(10, 6, f"Puissance 4 = {data[player1][3]}")

	if len(player2) > 10:
		playerFormat = player2[:10] + "..."
	else:
		playerFormat = player2
	printAt(12, 5, f"{playerFormat} :")
	printAt(13, 6, f"Devinette   = {data[player2][0]}")
	printAt(14, 6, f"Allumette   = {data[player2][1]}")
	printAt(15, 6, f"Morpion     = {data[player2][2]}")
	printAt(16, 6, f"Puissance 4 = {data[player2][3]}")