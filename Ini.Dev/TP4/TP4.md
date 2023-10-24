# Exercice 1

## Part 1

```python
def fibonnaci(nb : int) -> int:

	if nb == 0:
		return 0
	elif nb == 1:
		return 1
	else:
		return (fibonnaci(nb - 1) + fibonnaci(nb - 2))

if __name__ == "__main__":

	nb : int
	end : int

	end = 0
	nb = 0

	while end == 0:
		try:
			nb = int(input("Enter number : "))
			if nb < 0:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
			else:
				end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	for i in range(0, nb + 1):
		print("Value U", i, " is ", fibonnaci(i), sep="")
```

>J'utilise la formule de fibonnaci pour calculer les chiffre final

## Test

```
Enter number : 5
Value U0 is 0
Value U1 is 1
Value U2 is 1
Value U3 is 2
Value U4 is 3
Value U5 is 5
```

## Part 2

```python
def fibonnaci(nb : int) -> int:

	if nb == 0:
		return 0
	elif nb == 1:
		return 1
	else:
		return (fibonnaci(nb - 1) + fibonnaci(nb - 2))

if __name__ == "__main__":

	borne_sup : int
	end : int
	i : int
	result : int

	end = 0
	borne_sup = 0
	i = 0
	result = 0

	while end == 0:
		try:
			borne_sup = int(input("Enter borne_sup : "))
			if borne_sup < 0:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
			else:
				end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	while (result := fibonnaci(i)) < borne_sup:
		print("Value U", i, " is ", result, sep="")
		i += 1
```

>Même principe mais j'utilise une borne a la place

## Test

```
Enter borne_sup : 5
Value U0 is 0
Value U1 is 1
Value U2 is 1
Value U3 is 2
Value U4 is 3
```

# Exercice 2

```python
def is_prime(nb : int) -> bool:
	i : int

	i = 2

	if nb <= 1:
		return False
	while i < nb:
		if (not (nb % i)):
			return False
		i += 1
	return True
	
if __name__ == "__main__":

	nb : int
	end : int

	end = 0
	nb = 0

	while end == 0:
		try:
			nb = int(input("Enter number : "))
			if nb < 0:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
			else:
				end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	if is_prime(nb):
		print(nb, "est premier")
	else:
		print(nb, "n'est pas premier")
```

>Je check tout les chiffre jusqu'a ce que le nb soit divisible par autre chose que lui même ou 1, si c'est le cas alors ce n'est pas un chiffre premier

## Test

```python
Enter number : 5
5 est premier
```

```python
Enter number : 566
566 n'est pas premier
```

# Exercice 3

```python
if __name__ == "__main__":

	nb : int
	end : int
	i : int

	nb = 0
	end = 0
	i = 0

	while end == 0:
		try:
			nb = int(input("Enter number : "))
			if nb < 0:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
			else:
				end = 1
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")

	for i in range(1, nb * 2, 2):
		print(" " * (nb - i // 2) ,"*" * i)
```

>J'affiche le nombre de * par rapport a i et ensuite le nombre d'espace par rapport a nb et i

## Test

```
Enter number : 5
      *
     ***
    *****
   *******
  *********
```

# Exercice 4

```python
if __name__ == "__main__":

	day : int
	month : int
	year : int
	is_leap_year : bool
	end : int
	monthMaxDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	day = 0
	month = 0
	year = 0
	is_leap_year = False
	end = 0

	while end == 0:
		try:
			day = int(input("Enter number of days : "))
			if day > 0 and day <= 31:
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
			month = int(input("Enter number of months : "))
			if month > 0 and month <= 12:
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
			year = int(input("Enter number of years : "))
			if year > 0:
				end = 1
			else:
				end = 0
				print("ERROR[ValueError] : Value entered is not correct.")
		except ValueError:
			end = 0
			print("ERROR[ValueError] : Value entered is not correct.")
	
	day += 1
	if year // 4 and not (year // 100) or year // 400:
		is_leap_year = True
	if month == 2 and is_leap_year:
		monthMaxDays[1] = 28
	if month == 12 and day >= 31:
		day = 1
		month = 1
		year += 1
	if monthMaxDays[month - 1] < day:
		day = 1
		month += 1

	print(f"Tomorrow : {day} {month} {year}")
```

## Test

```
Enter number of days : 28
Enter number of months : 5
Enter number of years : 2023
Your date i : 29 5 2023
```