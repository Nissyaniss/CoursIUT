# Compte rendu TP2

## Exercice 1

```python
if __name__ == "__main__":
	number1	: float
	number2	: float
	end		: int

	number1 = 0

:
	number2 = 0
	end = 0

	while end == 0:
		try:
			number1 = int(input("Entrer number1 :\n"))
			end = 1
		except ValueError:
			print("Error : Invalid Value")
	end = 0
	while end == 0:
		try:
			number2 = int(input("Entrer number2 :\n"))
			end = 1
		except ValueError:
			print("Error : Invalid Value")

	if number1 < number2:
		print(f"{number1} < {number2}")
	elif number1 > number2:
		print(f"{number1} > {number2}")
	elif number1 == number2:
		print(f"{number1} = {number2}")
```

>Le but de cet exercice était de faire les différentes égalités entre deux nombres. <br>J'ai donc demandé les deux nombres a l'utilisateur (et vérifie qu'ils sont bien des chiffres), puis ensuite je les compare pour ensuite afficher leurs égalités

### Test
---
<br>

a:
```
Enter number1 :
a
Error : Invalid Value
Enter number1 :

```

5, 7:
```
Enter number1 :
5
Enter number2 :
7
5 < 7
```

-5, -7:
```
Enter number1 :
-5
Enter number2 :
-7
-5 > -7
```

## Exercice 2

```python
if __name__ == "__main__":
	print("Le nombre de plaque est 2. Pas de question.")
```

>En suivant l'énoncé de l'exercice on peut remarqué que la réponse 2 fonctionne dans absolument tout les cas.

## Exercice 3

```python
import math

if __name__ == "__main__":
	delta	: float
	x1		: float
	x2		: float
	a		: float
	b		: float
	c		: float
	end		: int

	a = 0
	b = 0
	c = 0
	end = 0

	print("With the form : ax^2 +bx + c.")
	while end == 0:
		try:
			a = float(input("Enter a : "))
			b = float(input("Enter b : "))
			c = float(input("Enter c : "))
			end = 1
		except ValueError:
			print("ERROR : Value incorrect")

	delta = pow(b, 2) - (4 * a * c)
	if delta == 0:
		x1 = -b / (2 * a)
		print(f"Your answer is x = {x1}")
	elif delta > 0:
		x1 = (-b - math.sqrt(delta)) / (2 * a)
		x2 = (-b + math.sqrt(delta)) / (2 * a)
		print(f"Your answer is x1 = {x1} and x2 = {x2}")
	elif delta < 0:
		print("ERROR : There is no solution")
```

>Le but de cette exercice était de résoudre toutes équations du second degré donc en premier lieu je demande a l'utilisateur a, b, c (de la forme ax<sup>2</sup> + bx + c) et je check si les valeurs sont bien des chiffres.<br>Par la suite je calcule le delta avec la formule (Δ = b<sup>2</sup> - 4ac) ensuite je vérifier si delta est égal à 0 ou supérieur a zéro pour déterminer mon résultat mais arrêter le programme si delta est inférieur à 0.<br>Avec delta égal à zero je sais que la solution est x = -b &divide; 2a (et je le calcule et l'affiche).<br>Pour delta supérieur à 0 on sait que les solution sont x1 = -b - &#8730;Δ &divide; 2a et x2 = -b + &#8730;Δ &divide; 2a (je les calcules et les affiches)

### Test
---
<br>

a:
```
With the form : ax^2 +bx + c.
Enter a : a
ERROR : Value incorrect
```

1, 2, 3:
```
With the form : ax^2 +bx + c.
Enter a : 1
Enter b : 2
Enter c : 3
ERROR : There is no solution
```

3, -6, -2:
```
With the form : ax^2 +bx + c.
Enter a : 3
Enter b : -6
Enter c : -2
Your answer is x1 = -0.29099444873580566 and x2 = 2.290994448735806
```

2, 3, 1.125:
```
With the form : ax^2 +bx + c.
Enter a : 2
Enter b : 3
Enter c : 1.125
Your answer is x = -0.75
```

## Exercice 4

```python
import os
import colorama

def correctNumber(numberToEnter : str, error : str) -> int :
	nb	: int
	end	: int

	end = 0
	nb = 0

	while end == 0:
		try:
			nb = int(input("Enter number of " + numberToEnter + " : "))
			if nb >= 0:
				end = 1
			else:
				print(colorama.Fore.RED + error + colorama.Fore.WHITE)
				os.system("clear||cls")
		except ValueError:
			os.system("clear||cls")
			print(colorama.Fore.RED + error + colorama.Fore.WHITE)
	return nb

def menu():
	print("Menu\n\n")
	print("Choose what you want to do :\n")
	print("\t1- Convert seconds into seconds/minutes/hours/days/month/year")
	print("\t2- Convert seconds/minutes/hours/days/month/year into seconds\n")

if __name__ == "__main__":
	seconds	: int
	minutes	: int
	hours	: int
	days	: int
	weeks	: int
	month	: int
	year	: int
	choice	: int
	end		: int

	seconds = 0
	minutes = 0
	hours = 0
	days = 0
	weeks = 0
	month = 0
	year = 0
	choice = 0
	end = 0

	menu()
	while end == 0:
		try:
			choice = int(input("Choose the number : "))
			if choice >= 1 and choice <= 2:
				end = 1
			else:
				os.system("clear||cls")
				print(colorama.Fore.RED + "ERROR : Incorrect Value, accepted value are [1], [2]" + colorama.Fore.WHITE)
				menu()
		except ValueError:
			os.system("clear||cls")
			print(colorama.Fore.RED + "ERROR : Incorrect Value, accepted value are [1], [2]" + colorama.Fore.WHITE)
			menu()
	if choice == 1:
		end = 0
		seconds = correctNumber("seconds", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		year = seconds // 31536000
		seconds = seconds % 3156000
		month = seconds // 2678400
		seconds = seconds % 2678400
		month = seconds // 604800
		seconds = seconds % 604800
		days = seconds // 86400
		seconds = seconds % 86400
		hours = seconds // 3600
		seconds = seconds % 3600
		minutes = seconds // 60
		seconds = seconds % 60
		print(f"Your time is {year}/{month}/{weeks}/{days} {hours}:{minutes}:{seconds}")
	if choice == 2:
		year = correctNumber("years", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		month = correctNumber("month", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		weeks = correctNumber("weeks", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		days = correctNumber("days", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		hours = correctNumber("hours", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		minutes = correctNumber("minutes", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)
		seconds = correctNumber("seconds", colorama.Fore.RED + "ERROR: Incorrect Value\n.Value must be a positive or null number" + colorama.Fore.WHITE)

		seconds =+ (year * 31536000) + (month * 3156000) + (weeks * 604800) + (days * 86400) + (hours * 3600) + (minutes * 60)
		print(f"Result is {seconds} seconds.")
```

>Pour commencer j'affiche le menu via `menu()` puis ensuite récupère le choix de l'utilisateur puis vérifie que celui-ci avec les options disponibles (1, 2).<br><br>Pour 1 :<br>Je demande le nombre de seconde et vérifie que celui-ci n'est pas négatif ou pas un nombre, après ca je calcul ce que ce nombre de seconde ferait en années/mois/jour/semaines/jours/heures/minutes/secondes puis j'affiche le tout.<br><br>Pour 2:<br>Je demande à l'utilisateur le nombre de années/mois/semaines/jours/heures/minutes/secondes et je convertie le tout en secondes pour ensuite l'afficher.

### Test
---
<br>

a:
```
ERROR : Incorrect Value, accepted value are [1], [2]
Menu


Choose what you want to do :

	1- Convert seconds into seconds/minutes/hours/days/month/year
	2- Convert seconds/minutes/hours/days/month/year into seconds

Choose the number : 
```
1, a:
```
ERROR: Incorrect Value
.Value must be a positive or null number
Enter number of seconds : 
```


1, 50000:
```
Menu


Choose what you want to do :

	1- Convert seconds into seconds/minutes/hours/days/month/year
	2- Convert seconds/minutes/hours/days/month/year into seconds
Choose the number : 1
Enter number of seconds : 50000
Your time is 0/0/0/0 13:53:20
```

2, 1, 1, 1, 1, 1, 1, 1
```
Menu


Choose what you want to do :

	1- Convert seconds into seconds/minutes/hours/days/month/year
	2- Convert seconds/minutes/hours/days/month/year into seconds

Choose the number : 2
Enter number of years : 1
Enter number of month : 1
Enter number of weeks : 1
Enter number of days : 1
Enter number of hours : 1
Enter number of minutes : 1
Enter number of seconds : 1
Result is 35386860 seconds.
```