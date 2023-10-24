import math

if __name__ == "__main__":
	temp			: str
	rayon			: float
	aire			: float
	perimetre		: float

	temp = ""
	rayon = 0.0
	aire = 0.0
	while temp == "":
		temp = input("Saisir le rayon: ")
		try:
			rayon = float(temp)
			if rayon <= 0:
				print(f"Erreur [ValueError]: Valeur rentrée incorrecte, veuillez recommencer. [{temp}]")
				temp = ""
		except ValueError:
			print(f"Erreur [ValueError]: Valeur rentrée incorrecte, veuillez recommencer. [{temp}]")
			temp = ""
	aire = round(math.pi * math.pow(rayon, 2), 2)
	perimetre = round(2 * math.pi * rayon, 2)
	print(f'Votre aire est {aire} . (aire = {round(math.pi, 2)} * {round(math.pow(rayon, 2), 2)}) \
	\nVotre périmètre est {perimetre} . (périmètre = 2 * {round(math.pi, 2)} * {rayon})')

