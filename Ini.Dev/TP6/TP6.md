# Exercice 1

## Code

```py
def checkAge(age : int, borneUp : int, borneDown: int, message : str, list : list[str]):
	if age >= borneDown and age < borneUp:
		list.append(message)

if __name__ == "__main__":
	date1Days		: int
	date1Months		: int
	date1Years		: int
	date2Days		: int
	date2Months		: int
	date2Years		: int
	age				: int
	criteria		: list[str]

date1Days = int(input("Enter day of date 1 : "))
date1Months = int(input("Enter month of date 1 : "))
date1Years = int(input("Enter year of date 1 : "))
date2Days = int(input("Enter day of date 2 : "))
date2Months = int(input("Enter month of date 2 : "))
date2Years = int(input("Enter year of date 2 : "))

if date1Years > date2Years:
	print("Date 1 superior to date 2")
elif date1Years == date2Years:
	if date1Months > date2Months:
		print("Date 1 superior to date 2")
	elif date1Months == date2Months:
		if date1Days > date2Days:
			print("Date 1 superior to date 2")
if date2Days == date1Days and date1Years == date2Years and date1Months == date2Months:
	print("Your just born dont go on a computer already !")

age = date2Years - date1Years
if date1Months > date2Months:
	age -= 1
elif date1Months == date2Months and date1Days > date2Days:
	age -= 1

criteria = []
print(age)
if age < 18:
	criteria.append("mineur")
elif age >= 18:
	criteria.append("majeur")
	checkAge(age, 30, 20, "vingtenaire", criteria)
	checkAge(age, 40, 30, "trentenaire", criteria)
	checkAge(age, 50, 40, "quadragénaire", criteria)
	checkAge(age, 60, 50, "quinquagénaire", criteria)
	checkAge(age, 70, 60, "sexagénaire", criteria)
	if age >= 65:
		criteria.append("retraitée")

for e in criteria:
	print(e)
```

## Explication

>Je check tout d'abord si la date 1 est inférieur a la date 2, ensuite je calcul le nombre d'année écoulée depuis date 1 et `append` a ma `list` les critère.

## Tests

```
Enter day of date 1 : 5  
Enter month of date 1 : 5
Enter year of date 1 : 5
Enter day of date 2 : 10
Enter month of date 2 : 10
Enter year of date 2 : 10
5
mineur
```

```
Enter day of date 1 : 1
Enter month of date 1 : 1
Enter year of date 1 : 1
Enter day of date 2 : 1
Enter month of date 2 : 1
Enter year of date 2 : 75
74
majeur
retraitée
```

# Exercice 2

## Code

```py
def sommeRRecursive(n : int) -> int:
	if n == 1:
		return 1
	else:
		return n + sommeRRecursive(n - 1)
	
def sommeRIterative(n : int) -> int:
	res : int
	
	res = 0

	while n > 1:
		res += n
		n -= 1
	return res + 1

if __name__ == "__main__":
	print(sommeRIterative(5))
	print(sommeRRecursive(5))
```

## Explications

>??

## Test

```
15
15
```

# Exercice 3

## Code

```py
def powerRecursive(a : int, n : int) -> int:
	x : int

	x = 0

	if n == 1:
		return a
	elif n % 2 == 0:
		x = powerRecursive(a, n // 2)
		return x * x
	elif n % 2 == 1:
		x = powerRecursive(a, (n - 1) // 2)
		return a * x * x
	return a

if __name__ == "__main__":
	print(powerRecursive(10, 10))
```

## Explication

>??

## Test

```
10000000000
```