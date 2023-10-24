-- CREATE TABLE JOUEUR(
--     idJoueur INT PRIMARY KEY NOT NULL,
--     nom VARCHAR(255) NOT NULL,
--     prenom VARCHAR(255) NOT NULL,
--     age INT NOT NULL,
--     nationnalite VARCHAR(255) NOT NULL,
-- );
-- CREATE TABLE TOURNOI(
--     idTournoi INT PRIMARY KEY NOT NULL,
--     tournoi VARCHAR(255) NOT NULL,
--     sponsor VARCHAR(255) NOT NULL,
-- );
-- CREATE TABLE GAIN(
--     idJoueur INT FOREIGN KEY REFERENCES JOUEUR(idJoueur) NOT NULL,
--     idTournoi INT FOREIGN KEY REFERENCES TOURNOI(idTournoi) NOT NULL,
--     annee INT NOT NULL,
--     montant DECIMAL(10, 2) NOT NULL,

--     PRIMARY KEY(idJoueur, idTournoi, annee)
-- );
-- CREATE TABLE MATCH(
--     idGagnant INT FOREIGN KEY REFERENCES JOUEUR(idJoueur) NOT NULL,
--     idPerdant INT FOREIGN KEY REFERENCES JOUEUR(idJoueur) NOT NULL,
--     idTournoi INT FOREIGN KEY REFERENCES TOURNOI(idTournoi) NOT NULL,
--     dateMatch DATE NOT NULL,
-- )

-- SELECT nom, SUM(montant) FROM JOUEUR, GAIN
-- WHERE JOUEUR.idJoueur = GAIN.idJoueur
-- GROUP BY nom, annee

-- SELECT nom, age FROM JOUEUR, MATCH, TOURNOI
-- WHERE JOUEUR.idJoueur = MATCH.idGagnant
-- AND TOURNOI.idTournoi = MATCH.idTournoi
-- AND YEAR(dateMatch) = 2020
-- AND tournoi = 'Garros'
-- UNION
-- SELECT nom, age FROM JOUEUR, MATCH, TOURNOI
-- WHERE JOUEUR.idJoueur = MATCH.idPerdant
-- AND TOURNOI.idTournoi = MATCH.idTournoi
-- AND YEAR(dateMatch) = 2020
-- AND tournoi = 'Garros'

-- SELECT DISTINCT nom, age FROM JOUEUR, MATCH, TOURNOI
-- WHERE JOUEUR.idJoueur = MATCH.idGagnant OR JOUEUR.idJoueur = MATCH.idPerdant
-- AND TOURNOI.idTournoi = MATCH.idTournoi
-- AND YEAR(dateMatch) = 2020
-- AND tournoi = 'Garros'

-- SELECT nom, nationnalite FROM JOUEUR, MATCH, TOURNOI
-- WHERE JOUEUR.idJoueur = MATCH.idGagnant
-- AND TOURNOI.idTournoi = MATCH.idTournoi
-- AND tournoi = 'Garros'
-- INTERSECT 
-- SELECT nom, nationnalite FROM JOUEUR, MATCH, TOURNOI
-- WHERE JOUEUR.idJoueur = MATCH.idGagnant
-- AND TOURNOI.idTournoi = MATCH.idTournoi
-- AND tournoi = 'Open'

-- SELECT nom, prenom FROM JOUEUR
-- WHERE idJoueur NOT IN
-- (
--     SELECT idGagnant FROM MATCH
-- )

-- SELECT nom, prenom FROM JOUEUR
-- WHERE idJoueur NOT IN
-- (
--     SELECT idGagnant FROM MATCH, TOURNOI
--     WHERE TOURNOI.idTournoi = MATCH.idTournoi
--     AND tournoi = 'Garros'
-- )

-- SELECT AVG(montant) FROM GAIN
-- WHERE idTournoi IN
-- (
--     SELECT idTournoi FROM TOURNOI
--     WHERE tournoi = 'Garros'
-- )
-- GROUP BY annee

-- SELECT SUM(montant) / COUNT(montant) FROM GAIN
-- WHERE idTournoi IN
-- (
--     SELECT idTournoi FROM TOURNOI
--     WHERE tournoi = 'Garros'
-- )
-- GROUP BY annee

-- SELECT nom, COUNT(idGagnant) FROM MATCH, JOUEUR
-- WHERE JOUEUR.idJoueur = MATCH.idGagnant
-- GROUP BY nom

-- SELECT DISTINCT J1.nom AS gagant, J2.nom AS perdant FROM JOUEUR J1, JoueuR J2, MATCH
-- WHERE J1.idJoueur = MATCH.idGagnant
-- AND J2.idJoueur = MATCH.idPerdant