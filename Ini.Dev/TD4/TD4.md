# Exercice 1

```
fonction estNbParfait(nb : entier) retourne bool
debut
	avec divNb : entier
		 i : entier

	divNb <- 0
	i     <- 0
		
	tant que i de 1 à nb / 2 faire
		si nb % i alors
			divNb <- divNb + i
		finsi
	fin faire
	
	si div = nb alors
		retourne Vrai
	sinon
		retourne Faux
	finsi
```

```
programme testFonction
debut

	avec nb : entier

	Afficher "Entrer le nombre dont vous voulez savoir si il est parfait ou non."
	Saisir nb
	Controle nb
	tant que i de 1 à nb
		si estNbParfait(nb) alors
			Afficher i, " est parfait."
		sinon
			Afficher i, " n'est pas parfait."
		finsi
	finfaire
```

# Exercice 2

```
fonction VerifierDate(jours : entier, mois : entier, annee : entier) -> bool
debut
	avec anneeBis : entier
		 fevrierOk : entier
		 moisOk : entier

	anneeBis <- (annee / 4 et annee mod 100 != 0) ou (annee mod 400 = 0)
	fevrierOk <- (anneeBis et jour <= 29) ou (non anneeBis et jour <= 28)
	moisOk <- (ect)
```

# Exercice 3

```
Procedure SaisirAmpoule(; val : entier)
debut

	Afficher "Saisir NbAmpoule"
	Saisir val
	Tant que (val < 10 et val mod 10 != 0) faire
		Afficher "Erreur"
		Afficher "Saisir NbAmpoule"
		Saisir val
	finfaire
fin SaisirAmpoule

Procedure Calcule (val : entier ;)
debut
	Avec G : entier
		 M : entier
		 P : entier

	G <- val / 200
	Afficher "Il faut", G, "grand cartons"
	val <- val - (G * 200)

	M <- val / 50
	Afficher "Il faut", M, "moyens cartons"
	val <- val - (M * 50)
	P <- val / 10
	Afficher "Il faut", P, "petits cartons"

programme ampoule
debut
	avec nbAmpoule : entier
		 choix : entier
	
	choix <- entier

	Tant que (choix != 3) faire
		Afficher "1 - Entrer le nombre d'ampoules"
		Afficher "2 - Calculer et afficher les emballages"
		Afficher "3 - Quitter"
		Saisir choix
		Selon choix faire
			cas '1' : SaisirNbAmpoule(; nbAmpoules)
			cas '2' : Calcul(nbAmpoule)
			cas '3' : Afficher "Au revoir."
			Defaut : Afficher "Erreur Choix"
		finfaire
	finfaire
fin ampoule

```
