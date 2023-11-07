# Exercice 1

```
programme 1
debut
	avec v[10] : reels
		 i : entier

	pour i de 0 a 9 pas 1 faire
		v[i] <- saisir Entrer un reel
	finfaire

	pour i de 9 a 0 pas -1 faire
		afficher v[i]
	finfaire
fin 1
```

```
programme 2
debut
	avec v[10] : entier
		 v1[10] : entier
		 temp : entier
		 i : entier

	pour i de 0 a 9 pas 1 faire
		saisir v[i]

	pour i de 0 a 9 pas 1 faire
		saisir v1[i]
	
	pour i de 0 a 9 pas 1 faire
		afficher v[i] + v1[i]

	pour i de 0 a 9 pas 1 faire
		temp <- temp + v[i] * v1[i]
	
	afficher temp
fin 2
```

```
programme 3
debut
	avec v[10] : entier
		 temp : entier
		 i : entier
	
	pour i de 0 a 9 pas 1 faire
		saisir v[i]
	finfaire

	pour i de 0 a 9 pas 1 faire
		temp <- temp + v[i] * v[i]
	finfaire

	afficher temp

	pour i de 0 a 9 pas 1 faire
		v[i] <- v[i] / temp
	finfaire

	pour i de 0 a 9 pas 1 faire
		afficher v[i]
	finfaire
fin 3
```

```
programme 4
debut
	avec v[3] : entier
		 v1[3] : entier
		 res[3] : entier
		 i : entier
	
	pour i de 0 a 2 pas 1 faire
		saisir v[i]
	finfaire

	pour i de 0 a 2 pas 1 faire
		saisir v1[i]
	finfaire

	res[0] <- v[1] * v1[2] - v[2] * v1[1]
	res[1] <- v[2] * v1[0] - v[0] * v1[2]
	res[2] <- v[0] * v1[1] - v[1] * v1[0]

	pour i de 0 a 2 pas 1 faire
		afficher res[i]
	finfaire
fin 4
```

## Exercice 2

```
programme exercice2
debut

	avec nbr[1000] : entier
		 currentNbr : entier
		 userInput : entier
		 count : entier
		 i : entier
		 rand : entier
		 rand1 : entier
	
	currentNbr <- 0
	UserInput <- 0
	count <- 0

	tant que userInput >= 0 faire
		saisir userInput
		nbr[i] <- userInput
		i <- i + 1
	finfaire

	pour i de 0 a 999 pas 1 faire
		currentNbr <- nbr[i]
		si currentNbr >= 0 alors
			count <- count + 1
		sinon
			i <- 999
		finsi
	finfaire

	pour i de 0 a count pas 1 faire
		rand <- entier(random()) * count
		rand1 <- entier(random()) * count

		temp <- nbr[test]
		nbr[test] <- nbr[test1]
		nbr[test1] <- temp
	finfaire
fin exercice2
```