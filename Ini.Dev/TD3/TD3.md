# Exercice 1

## Part 1

>Faire un prog qui affiche tout les chiffres de la suite de Fibonacci entre U0 et  Un (n étant entré par l'utilisateur)

```
programme fibonnaci
debut

	Avec nbterme : entier
		 i : entier
		 Un : entier
		 Un1 : entier
		 Un2 : entier
		 termeCurrent : entier

	Afficher "Saisir nombre de termes : "
	Saisir nbterme
	Contrôler nbterme > 0

	Un <- 0
	Un1 <- 1
	i <- 0

	Afficher "U0 = ", Un
	Si nbterme >= 1 alors
		Afficher "U1 = ", Un1
	Pour i de 2 a nbterme faire:
		Un2 <- Un + Un1
		Afficher "U", i, " = ", Un2
		Un <- Un1
		Un1 <- Un2
```

## Part 2

>Même histoire sauf que a la place de faire U0 a Un l'utilisateur rentre Un et non n

```
programme fibonnaci
debut

	Avec borne : entier
		 i : entier
		 Un : entier
		 Un1 : entier
		 Un2 : entier
		 termeCurrent : entier

	Afficher "Saisir borne : "
	Saisir borne
	Contrôler borne > 0

	Un <- 0
	Un1 <- 1
	i <- 3

	Afficher "U0 = ", Un
	Si born = 1 alors
		Afficher "U1 = ", Un1
		Afficher "U2 = ", Un1
	Tant que Un2 <= borne faire
		Afficher "U", i " = ", Un2
		Un <- Un1
		Un1 <- Un2
		Un2 <- Un + Un1
		i <- i + 1
	finfaire
```

# Exercice 2

>Faire un prog qui donne tout les diviseur d'un chiffre (par exemple 4 -> 1 2 4)

```
programme diviseurs
debut

	avec nb : entier

	Afficher "Saisir un entier positif: "
	Saisir nb
	Contrôler nb > 0

	Afficher "Les diviseurs sont :"
	pour i de 1 a nb faire
		si nb mod i = 0
			Afficher i
		finsi
	finfaire
fin prog diviseurs
```

# Exercice 3

>Faire un prog qui dit si le nb rentrer est un chiffre premier

```
fonction f_premier(nb : entier) retourne entier
debut
		avec i : entier

		tant que i <= sqrt(n) faire
			si n mod i = 0 alors
				retourne 0
			finsi
		finfaire
	retourne 1
fin f_premier

programme premier
debut

	avec nb : entier
		 estPremier : entier

	Afficher "Saisir un entier positif : "
	Saisir nb
	Contrôler nb > 0

	estPremier <- f_premier(nb)

	si estPremier = 1 alors
		Afficher "L'entier ", nb, " est premier"
	sinon
		Afficher "L'entier ", nb, " n'est pas premier"
	finsi
fin prog premier
```