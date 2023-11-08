-- SELECT COUNT(idPerdant) AS NbrMatchJouer FROM MATCHDOUBLES

-- SELECT DISTINCT idJoueur FROM JOUEUR, MATCHDOUBLES, MATCH
-- WHERE (idJoueur = MATCHDOUBLES.idPerdant
-- OR idJoueur = MATCHDOUBLES.idPerdant2
-- OR idJoueur = MATCHDOUBLES.idGagnant
-- OR idJoueur = MATCHDOUBLES.idGagnant2)
-- AND
-- (idJoueur = MATCH.idPerdant
-- OR idJoueur = MATCH.idGagnant)
-- AND MATCH.dateMatch BETWEEN '2021-01-01' AND '2021-12-31'

-- SELECT nom, prenom, COUNT(idJoueur) AS NbrMatchJouer FROM (
--     SELECT nom, prenom, idJoueur FROM JOUEUR, MATCHDOUBLES
--     WHERE (idJoueur = MATCHDOUBLES.idGagnant2
--     OR idJoueur = MATCHDOUBLES.idGagnant)
--     UNION ALL
--     SELECT nom, prenom, idJoueur FROM JOUEUR, MATCH
--     WHERE idJoueur = MATCH.idGagnant
-- ) TOTO
-- GROUP BY nom, prenom


SELECT DISTINCT
CASE
    WHEN j1.nom < j2.nom THEN j1.nom
    ELSE j2.nom
END AS nom1,
CASE
    WHEN j1.nom < j2.nom THEN j2.nom
    ELSE j1.nom
END AS nom2
FROM JOUEUR j1, JOUEUR j2, MATCHDOUBLES, MATCH
WHERE
    j1.idJoueur != j2.idJoueur AND
    (
    (j1.idJoueur = MATCHDOUBLES.idGagnant OR j1.idJoueur = MATCHDOUBLES.idGagnant2)
    AND (j2.idJoueur = MATCHDOUBLES.idGagnant2 OR j2.idJoueur = MATCHDOUBLES.idGagnant)
    OR
    (j1.idJoueur = MATCHDOUBLES.idPerdant OR j1.idJoueur = MATCHDOUBLES.idPerdant2)
    AND (j2.idJoueur = MATCHDOUBLES.idPerdant2 OR j2.idJoueur = MATCHDOUBLES.idPerdant)
    )
INTERSECT
SELECT DISTINCT
CASE
    WHEN j1.nom < j2.nom THEN j1.nom
    ELSE j2.nom
END AS nom1,
CASE
    WHEN j1.nom < j2.nom THEN j2.nom
    ELSE j1.nom
END AS nom2
FROM JOUEUR j1, JOUEUR j2, MATCH
WHERE
    (
    (j1.idJoueur = MATCH.idGagnant)
    AND (j2.idJoueur = MATCH.idPerdant)
    OR
    (j1.idJoueur = MATCH.idPerdant)
    AND (j2.idJoueur = MATCH.idGagnant)
    )