import json
from termUtils import setTermCursor
from os import get_terminal_size

def isPlayerExisting(player : str) -> bool:
	"""
	La fonction `isPlayerExisting` vérifie si un joueur existe dans le fichier JSON contenant les
	données des joueurs.
	
	@param player Le paramètre "player" est une chaîne qui représente le nom du joueur.
	
	@return La fonction isPlayerExisting renvoie une valeur booléenne. Elle renvoie True si le joueur
	existe dans le dictionnaire de données, et False sinon.
	"""

	data : dict[str, tuple[int, int, int, int]]

	with open("players.json", "r") as jsonFile:
		data = json.load(jsonFile)
	
	if player in data:
		return True
	else:
		return False
	
def addPlayer(player : str) -> None:
	"""
	La fonction `addPlayer` ajoute un nouveau joueur au fichier JSON contenant les données des
	joueur.
	
	@param player Le paramètre "player" est une chaîne qui représente le nom du joueur que vous
	souhaitez ajouter aux données.
	"""

	data : dict[str, tuple[int, int, int, int]]

	with open("players.json", "r") as jsonFile:
		data = json.load(jsonFile)

	data.update({player : (0,0,0,0)})

	with open("players.json", "w") as outputFile:
		json.dump(data, outputFile, sort_keys=True, indent='\t', separators=(',',': '))

def addPoint(player : str, game : int) -> None:
	"""
	La fonction "addPoint" prend en paramètres le nom d'un joueur et un numéro de jeu pour rajouter
	1 point a jeu en question, au joueur en question.
	
	@param player Une chaîne représentant le nom du joueur qui a marqué un point dans le jeu.
	@param game Un nombre entier représentant le jeux ou le point a été gagné.
	"""

	data : dict[str, tuple[int, int, int, int]]

	with open("players.json", "r") as jsonFile:
		data = json.load(jsonFile)

	playerData = data[player]
	if game == 1:
		playerData = (playerData[0] + 1, playerData[1], playerData[2], playerData[3])
	elif game == 2:
		playerData = (playerData[0], playerData[1] + 1, playerData[2], playerData[3])
	elif game == 3:
		playerData = (playerData[0], playerData[1], playerData[2] + 1, playerData[3])
	else:
		playerData = (playerData[0], playerData[1], playerData[2] + 1, playerData[3])

	data[player] = playerData
	with open("players.json", "w") as outputFile:
		json.dump(data, outputFile, sort_keys=True, indent='\t', separators=(',',': '))

def printScoreboard() -> None:
	"""
	La fonction "printScoreboard" est utilisée pour imprimer un scoreboard de toute les parties
	gagnées dans les different jeu.
	"""
	i : int
	maxHeight : int

	i = 0
	maxHeight = get_terminal_size().lines - 3

	data : dict[str, tuple[int, int, int, int]]

	with open("players.json", "r") as jsonFile:
		data = json.load(jsonFile)
	
	for key, value in data.items():
		setTermCursor(6 + i , 5, f"{key} :")
		setTermCursor(6 + i + 1, 6, f"Devinette = {value[0]}")
		setTermCursor(6 + i + 2, 6, f"Allumette = {value[1]}")
		setTermCursor(6 + i + 3, 6, f"Morpion = {value[2]}")
		setTermCursor(6 + i + 4, 6, f"Puissance 4 = {value[3]}")
		i = i + 6
		if i + 6 >= maxHeight - 6:
			setTermCursor(maxHeight - 2, 5, "...")
			break