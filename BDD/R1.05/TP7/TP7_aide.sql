--Utilisation d'une sous-requete

-- SELECT AVG(age) as ageMoyen FROM
-- (
--     SELECT DISTINCT nom, prenom, age FROM JOUEUR JOIN MATCH ON idJoueur=idGagnant
-- ) aliasTable


--Conditions dans un SELECT avec CASE

SELECT 
CASE 
    WHEN age<20 THEN 'mois de 20 ans'
    WHEN age<30 THEN 'mois de 30 ans'
    ELSE '30 ans ou plus'
END AS groupeAge
FROM JOUEUR