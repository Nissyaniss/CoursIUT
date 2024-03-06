# Exercice 1

1)
> Sur feuille

2)
```sql
CREATE TABLE GAIN (
	idJoueur INT FOREIGN KEY REFERENCES JOUEUR.idJoueur NOT NULL,
	idTournoi INT FOREIGN KEY REFERENCES TOURNOI.idTournoi NOT NULL,
	annee INT NOT NULL,
	montant DECIMAL(6, 2) PRIMARY KEY NOT NULL,

	PRIMARY KEY(idJoueur, idTournoi, annee)
)
```

# Exercice 2

1)
```sql
SELECT nom, gains, annee FROM JOUEUR, TOURNOI, GAIN
WHERE JOUEUR.idJoueur = GAIN.idJoueur
AND TOURNOI.idTournoi = GAIN.idTournoi
ORDER BY nom DESC
ORDER BY annee DESC
GROUP BY annee
```

2)
```sql

SELECT nom, age FROM JOUEUR
WHERE idJoueur NOT IN
(
	SELECT idGagnant, idPerdant, idTournoi FROM MATCH, TOURNOI
	WHERE MATCH.idGagnant = JOUEUR.idJoueur
	AND MATCH.idPerdant = JOUEUR.idJoueur
	AND MATCH.idTournoi = TOURNOI.idTournoi
	AND TOURNOI.tournoi != "Garros"
	AND MATCH.dateMatch >= '01/01/2020'
	AND MATCH.dateMatch < '01/01/2021'
)
UNION
SELECT DISTINCT nom, age FROM JOUEUR
```

3)
```sql
SELECT nom, age FROM JOUEUR
WHERE idJoueur NOT IN
(
	SELECT idGagnant, idPerdant, idTournoi FROM MATCH, TOURNOI
	WHERE MATCH.idGagnant = JOUEUR.idJoueur
	AND MATCH.idPerdant = JOUEUR.idJoueur
	AND MATCH.idTournoi = TOURNOI.idTournoi
	AND TOURNOI.tournoi != "Garros"
	AND MATCH.dateMatch >= '01/01/2020'
	AND MATCH.dateMatch < '01/01/2021'
)
```

4)
```sql
SELECT nom, nationalite FROM JOUEUR
WHERE MATCH.idGagnant = JOUEUR.idJoueur
AND MATCH.idPerdant = JOUEUR.idJoueur
```