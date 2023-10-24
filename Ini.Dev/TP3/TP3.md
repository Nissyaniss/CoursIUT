# TP 3

## Exercice 1

### Code
---
<br>

```python
if __name__ == "__main__":
	nb1		: float
	nb2		: float
	result	: float
	end		: int
	sign	: str

	nb1 = 0
	nb2 = 0
	result = 0
	end = 0
	sign = ""

	while end == 0:
		try:
			nb1 = float(input("Enter number 1 : "))
			end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	end = 0
	while end == 0:
		try:
			nb2 = float(input("Enter number 2 : "))
			end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	end = 0
	while end == 0:
		sign = input("Enter sign : ")
		if sign == "*" or sign == "/" or sign == "+" or sign == "-":
			end = 1
		else:
			print("ERROR[ValueError] : Value accepted : [+], [-], [*], [/]")
			end = 0

	if sign == "*":
		result = nb1 * nb2
	elif sign == "/":
		result = nb1 / nb2
	elif sign == "+":
		result = nb1 + nb2
	elif sign == "-":
		result = nb1 - nb2

	print(f"The result of {nb1} {sign} {nb2} is {result}")
```

### Explication
---
<br>

> En premier lieux je fait un check des variables saisit par l'utilisateur, ensuite je vérifie le signe et calcule en fonction de celui-ci pui affiche le résultat

### Tests
---
<br>

5 * 5:
```
Enter number 1 : 5
Enter number 2 : 5
Enter sign : *
The result of 5.0 * 5.0 is 25.0
```

5 * -5:

```
Enter number 1 : 5
Enter number 2 : -5
Enter sign : *
The result of 5.0 * -5.0 is -25.0
```

5 * 5.5:

```
Enter number 1 : 5
Enter number 2 : 5.5
Enter sign : *
The result of 5.0 * 5.5 is 27.5
```

5 + 5:
```
Enter number 1 : 5
Enter number 2 : 5
Enter sign : +
The result of 5.0 + 5.0 is 10.0
```

5 - 5:
```
Enter number 1 : 5
Enter number 2 : 5
Enter sign : -
The result of 5.0 - 5.0 is 0.0
```

5 / 3:
```
Enter number 1 : 5
Enter number 2 : 3
Enter sign : /
The result of 5.0 / 3.0 is 1.6666666666666667
```

## Exercice 2

### Code
---
<br>

```python
def ft_gdc(nb1 : int, nb2 : int) -> int:
	if nb1 != 0 and nb2 != 0:
		nb1 = nb1 % nb2
		nb1 = ft_gdc(nb2, nb1)

	return nb1

if __name__ == "__main__":
	nb1	: int
	nb2	: int
	gdc	: int
	end	: int
	tmp	: int

	nb1 = 0
	nb2 = 0
	gdc = 0
	end = 0
	tmp = 0

	while end == 0:
		try:
			nb1 = int(input("Enter number 1 : "))
			end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	end = 0
	while end == 0:
		try:
			nb2 = int(input("Enter number 2 : "))
			end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")

	if nb1 == nb2:
		result = nb1

	result = ft_gdc(nb1, nb2)
	print(f"The result is {result}")
```

### Explication
---
<br>

> Même histoire que l'exercice 1 au niveau des check, par la suite j'utilise de la récursivité avec ma fonction `ft_gdc` dans celle ci je check si mes 2 nombre ne sont pas 0 car si c'est le cas la réponse sera 0, si ce n'est pas le cas alors je modulo nb1 par nb2 puis rappelle la fonction en inversant les chiffre, tout ca jusqu'a obtenir 0 et donc prendre le chiffre avant ca qui sera le résultat

### Tests
---
<br>

48 18:

```
Enter number 1 : 48
Enter number 2 : 18
The result is 6
```

-5 2:

```
Enter number 1 : 5
Enter number 2 : -2
The result is -1
```

0 0:
```
Enter number 1 : 0
Enter number 2 : 0
The result is 0
```

## Exercice 3

### Code
---
<br>

```python
if __name__ == "__main__":
	years		: int
	months		: int
	days		: int
	end			: int
	isLeapYear	: int

	years = 0
	months = 0
	days = 0
	end = 0
	isLeapYear = 0

	while end == 0:
		try:
			days = int(input("Enter number of days : "))
			if days > 0:
				end = 1
			else:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	end = 0
	while end == 0:
		try:
			months = int(input("Enter number of months : "))
			if months > 0:
				end = 1
			else:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	end = 0
	while end == 0:
		try:
			years = int(input("Enter number of years : "))
			if years > 0:
				end = 1
			else:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")

	if months > 12:
		print("This date doesn't exist !")
		exit(0)
	if days > 31:
		print("This date doesn't exist !")
		exit(0)
	if months == 4 or months == 6 or months == 9 or months == 11:
		if days > 30:
			print("This date doesn't exist !")
			exit(0)
	if (years % 4 == 0 and years % 100 > 0) or years % 400 == 0:
		isLeapYear = 1
	if months == 2:
		if isLeapYear == 1:
			if days > 29:
				print("This date doesn't exist !")
				exit(0)
		else:
			if days > 28:
				print("This date doesn't exist !")
				exit(0)
	print("This date exists !")
```

### Explications
---
<br>

> Même histoire de check que dans les 2 exercices precedent, pour le résultat je fait juste quelque check (si mois > 12, si année bissextile alors février max jour = 29 ect)

### Tests
---
<br>

35 02 2004:

```
Enter number of days : 35
Enter number of months : 02
Enter number of years : 2004
This date doesn't exist !
```

-5 -5 -5:

```
Enter number of days : -5
ERROR[ValueError] : Value entered is not correct.
Enter number of days : 
```

0 0 0:

```
Enter number of days : 0
ERROR[ValueError] : Value entered is not correct.
Enter number of days : 
```

27 04 2004:

```
Enter number of days : 27
Enter number of months : 04
Enter number of years : 2004
This date exists !
```

29 02 2008:

```
Enter number of days : 29
Enter number of months : 02
Enter number of years : 2008
This date exists !
```

29 02 2009:

```
Enter number of days : 29
Enter number of months : 02
Enter number of years : 2009 
This date doesn't exist !

```