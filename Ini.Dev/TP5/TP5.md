# Exercice 1

## Code

```python
def nb_parfait(nb : int) -> bool:
	i : int
	res : int

	i = 0
	res = 0

	for i in range(1, nb // 2 + 1):
		if not (nb % i):
			res = res + i
	return res == nb

if __name__ == "__main__":
	nb : int
	end : bool
	i : int

	nb = 0
	end = False
	i = 0

	while not end:
		try:
			nb = int(input("Enter n : "))
			if nb > 0:
				end = True
			else: 
				end = False
				print("Negative numbers not accepted!")
		except ValueError:
			end = False
			print("Not a number!")
	for i in range(1, nb + 1): 
		if nb_parfait(i):
			print(f"{i} is perfect!")
		else:
			print(f"{i} is not perfect!")
```

## Explications

> J'ai fait une fonction qui permet de checker si un nombre est parfait en additionnant tout les diviseurs du nombre entré.

## Test

```
Enter n : 28
1 is not perfect!
2 is not perfect!
3 is not perfect!
4 is not perfect!
5 is not perfect!
6 is perfect!
7 is not perfect!
8 is not perfect!
9 is not perfect!
10 is not perfect!
11 is not perfect!
12 is not perfect!
13 is not perfect!
14 is not perfect!
15 is not perfect!
16 is not perfect!
17 is not perfect!
18 is not perfect!
19 is not perfect!
20 is not perfect!
21 is not perfect!
22 is not perfect!
23 is not perfect!
24 is not perfect!
25 is not perfect!
26 is not perfect!
27 is not perfect!
28 is perfect!
```

# Exercice 2

## Code 

```
if __name__ == "__main__":
	isLeapYear : bool
	isGood : bool
	end : bool
	days : int
	months : int
	years : int

	isLeapYear = False
	isGood = True
	end = False
	days = 0
	months = 0
	years = 0

	while not end:
		try:
			days = int(input("Enter number of days :"))
			if days < 31 and days > 0:
				end = True
			else: 
				end = False
				print("Negative or numbers superior to 31 are not accepted!")
		except ValueError:
			end = False
			print("Not a number!")
	end = False
	while not end:
		try:
			months = int(input("Enter number of months :"))
			if months < 13 and months > 0:
				end = True
			else: 
				end = False
				print("Negative or numbers superior to 12 are not accepted!")
		except ValueError:
			end = False
			print("Not a number!")
	end = False
	while not end:
		try:
			years = int(input("Enter n :"))
			if years > 1583:
				end = True
			else: 
				end = False
				print("Negative or numbers inferior to 1583 are not accepted!")
		except ValueError:
			end = False
			print("Not a number!")


	isLeapYear = (not (years % 4) > 1 and (years % 100) != 0) or (not (years % 400))

	match months:
		case 1: isGood = days <= 31
		case 2: isGood = (isLeapYear and days <= 29) or (not (isLeapYear) and days <= 28)
		case 3: isGood = days <= 31
		case 4: isGood = days <= 30
		case 5: isGood = days <= 31
		case 6: isGood = days <= 30
		case 7: isGood = days <= 31
		case 8: isGood = days <= 31
		case 9: isGood = days <= 30
		case 10: isGood = days <= 31
		case 11: isGood = days <= 30
		case 12: isGood = days <= 31
		case _: isGood = False

	#G LE DROIT AU IF MTN
	if isGood:
		print("Your date is correct!")
	else:
		print("Your date is not correct!")
```

## Explications

> Je check d'abord si l'année entrée est une année bissextile et ensuite je check par mois et si le jour est pas le bon par rapport au mois alors la date est fausse.

## Tests

```
Enter number of days :5
Enter number of months :6
Enter n :2023
Your date is correct!
```

```
Enter number of days :29
Enter number of months :2
Enter n :2023
Your date is not correct!
```

# Exercice 3

## Code

```python
if __name__ == "__main__":
	end : bool
	nb : int

	end = False
	nb = 0

	while not end:
		try:
			nb = int(input("Enter nb :"))
			if nb > 0:
				end = True
			else: 
				end = False
				print("Negative numbers are not accepted!")
		except ValueError:
			end = False
			print("Not a number!")
	
	for i in range(1, nb + 1):
		for y in range(1, i + 1):
			print(f"{y} ", end="")
		print("")
```

## Explication

> Je print tout les chiffre entre 1 et nb avec 1 de décalage a chaque fois.

# Exercice 4

## Code

```python
if __name__ == "__main__":
	end : bool
	nb : int
	lines : int
	cols : int
	i : int
	loops : int
	is2Part : bool
	spaces : int

	end = False
	nb = 1000
	lines = 0
	cols = 0
	loops = 0
	i = 0
	is2Part = False

	while not end:
		try:
			nb = int(input("Enter nb : "))
			if nb > 0:
				end = True
			else: 
				end = False
				print("Negative numbers are not accepted!")
		except ValueError:
			end = False
			print("Not a number!")

	spaces = len(str(nb * 2)) + 1

	i = nb * 2
	while loops != nb * 2 + 1:
		while cols != nb * 2 + 1:
			if cols < nb:
				print(" " * (len(str(nb * 2)) - len(str(i - lines)) - cols) + f"{i - lines}" + " " * (spaces - len(str(i - 1 - lines))), end='')
				i = i - 1
			elif cols == nb:
				print(f"{nb - lines}" + " " * (spaces - len(str(nb + 1 - lines))), end='')
				i = nb + 1
			elif cols <= nb * 2 + 1:
				print(f"{i - lines}" + " " * (spaces - len(str(i + 1 - lines))) , end='')
				i = i + 1
			cols = cols + 1
		print("")
		if lines == nb and not is2Part:
			lines = nb - 1
			is2Part = True
		elif is2Part:
			lines = lines - 1
		else:
			lines = lines + 1
		i = nb * 2
		loops = loops + 1
		cols = 0
```

## Explication

> Après avoir trouver le pattern de la ligne ((nb * 2) (nb * 2 - 1) (nb * 2 - 2) ... (nb * 2 - nb - 1) nb (nb * 2) (nb + 1) (nb + 2) ... (nb * 2)) j'ai ensuite incorporer les lignes car a chaque ligne avant le milieu + 1 descend de 1 et après milieu il monte de 1.

## Tests

```
8   7   6   5   4   5   6   7   8
7   6   5   4   3   4   5   6   7
6   5   4   3   2   3   4   5   6
5   4   3   2   1   2   3   4   5
4   3   2   1   0   1   2   3   4
5   4   3   2   1   2   3   4   5
6   5   4   3   2   3   4   5   6
7   6   5   4   3   4   5   6   7
8   7   6   5   4   5   6   7   8
```

```
30  29  28  27  26  25  24  23  22  21  20  19  18  17  16  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  
29  28  27  26  25  24  23  22  21  20  19  18  17  16  15  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  
28  27  26  25  24  23  22  21  20  19  18  17  16  15  14  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  
27  26  25  24  23  22  21  20  19  18  17  16  15  14  13  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  
26  25  24  23  22  21  20  19  18  17  16  15  14  13  12  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  
25  24  23  22  21  20  19  18  17  16  15  14  13  12  11  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  
24  23  22  21  20  19  18  17  16  15  14  13  12  11  10  9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  
23  22  21  20  19  18  17  16  15  14  13  12  11  10  9   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  
22  21  20  19  18  17  16  15  14  13  12  11  10  9   8   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  
21  20  19  18  17  16  15  14  13  12  11  10  9   8   7   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  
20  19  18  17  16  15  14  13  12  11  10  9   8   7   6   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  
19  18  17  16  15  14  13  12  11  10  9   8   7   6   5   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  
18  17  16  15  14  13  12  11  10  9   8   7   6   5   4   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  
17  16  15  14  13  12  11  10  9   8   7   6   5   4   3   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  
16  15  14  13  12  11  10  9   8   7   6   5   4   3   2   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  
15  14  13  12  11  10  9   8   7   6   5   4   3   2   1   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  
16  15  14  13  12  11  10  9   8   7   6   5   4   3   2   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  
17  16  15  14  13  12  11  10  9   8   7   6   5   4   3   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  
18  17  16  15  14  13  12  11  10  9   8   7   6   5   4   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  
19  18  17  16  15  14  13  12  11  10  9   8   7   6   5   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  
20  19  18  17  16  15  14  13  12  11  10  9   8   7   6   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  
21  20  19  18  17  16  15  14  13  12  11  10  9   8   7   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  
22  21  20  19  18  17  16  15  14  13  12  11  10  9   8   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  
23  22  21  20  19  18  17  16  15  14  13  12  11  10  9   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  
24  23  22  21  20  19  18  17  16  15  14  13  12  11  10  9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  
25  24  23  22  21  20  19  18  17  16  15  14  13  12  11  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  
26  25  24  23  22  21  20  19  18  17  16  15  14  13  12  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  
27  26  25  24  23  22  21  20  19  18  17  16  15  14  13  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  
28  27  26  25  24  23  22  21  20  19  18  17  16  15  14  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  
29  28  27  26  25  24  23  22  21  20  19  18  17  16  15  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  
30  29  28  27  26  25  24  23  22  21  20  19  18  17  16  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30 
```