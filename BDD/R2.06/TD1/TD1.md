# Opérations ensemblistes

## 1

|book_id|title|year|
|:-:|:-:|:-:|
|1|Les Illusions perdues|1837|
|2|Mémoires d'outre-tombe|1849|
|5|L'Illusion comique|1636|
|6|Andromaque|1667|
|1|Les Illusions perdues|1837|
|3|Le Petit chose|1868|
|5|L'Illusion comique|1636|

## 2

|book_id|title|year|
|:-:|:-:|:-:|
|1|Les Illusions perdues|1837|
|2|Mémoires d'outre-tombe|1849|
|5|L'Illusion comique|1636|
|6|Andromaque|1667|
|3|Le Petit chose|1868|

## 3

> `UNION ALL`sélectionne tous les enregistrements de chaque sous-requête même les doublons. Alors que `UNION` ne sélectionne sans les doublons.
```sql
SELECT DISTINCT * FROM (
    SELECT * FROM library.classical_books
    UNION ALL
    SELECT * FROM library.contemporary_books
);
```

## 4

|book_id|title|year|
|:-:|:-:|:-:|
|1|Les Illusions perdues|1837|
|5|L'Illusion comique|1636|

## 5

|book_id|title|year|
|:-:|:-:|:-:|
|2|Mémoires d'outre-tombe|1849|
|6|Andromaque|1667|
|3|Le Petit chose|1868|

# Jointures

## 1

|book_id|author_id|title|year|author_id|firstname|lastname|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|3|Les Illusions perdues|1837|1|François-René|de Chateaubriand|
|1|3|Les Illusions perdues|1837|2|Victor|Hugo|
|1|3|Les Illusions perdues|1837|3|Honoré|de Balzac|
|2|3|Mémoires d'outre-tombe|1849|1|François-René|de Chateaubriand|
|2|3|Mémoires d'outre-tombe|1849|2|Victor|Hugo|
|2|3|Mémoires d'outre-tombe|1849|3|Honoré|de Balzac|
|3|4|Le Petit chose|1868|1|François-René|de Chateaubriand|
|3|4|Le Petit chose|1868|2|Victor|Hugo|
|3|4|Le Petit chose|1868|3|Honoré|de Balzac|
|4|3|La Peau du chagrin|1831|1|François-René|de Chateaubriand|
|4|3|La Peau du chagrin|1831|2|Victor|Hugo|
|4|3|La Peau du chagrin|1831|3|Honoré|de Balzac|

|book_id|author_id|title|year|author_id|firstname|lastname|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|3|Les Illusions perdues|1837|1|François-René|de Chateaubriand|
|1|3|Les Illusions perdues|1837|2|Victor|Hugo|
|1|3|Les Illusions perdues|1837|3|Honoré|de Balzac|
|2|3|Mémoires d'outre-tombe|1849|1|François-René|de Chateaubriand|
|2|3|Mémoires d'outre-tombe|1849|2|Victor|Hugo|
|2|3|Mémoires d'outre-tombe|1849|3|Honoré|de Balzac|
|3|4|Le Petit chose|1868|1|François-René|de Chateaubriand|
|3|4|Le Petit chose|1868|2|Victor|Hugo|
|3|4|Le Petit chose|1868|3|Honoré|de Balzac|
|4|3|La Peau du chagrin|1831|1|François-René|de Chateaubriand|
|4|3|La Peau du chagrin|1831|2|Victor|Hugo|
|4|3|La Peau du chagrin|1831|3|Honoré|de Balzac|

## 2

|book_id|author_id|title|year|author_id|firstname|lastname|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|3|Les Illusions perdues|1837|2|Victor|Hugo|
|2|3|Mémoires d'outre-tombe|1849|1|François-René|de Chateaubriand|
|4|3|La Peau du chagrin|1831|3|Honoré|de Balzac|

## 3

|book_id|author_id|title|year|firstname|lastname|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|3|Les Illusions perdues|1837|Victor|Hugo|
|2|3|Mémoires d'outre-tombe|1849|François-René|de Chateaubriand|
|4|3|La Peau du chagrin|1831|Honoré|de Balzac|

## 4

|book_id|author_id|title|year|firstname|lastname|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|3|Les Illusions perdues|1837|Victor|Hugo|
|2|3|Mémoires d'outre-tombe|1849|François-René|de Chateaubriand|
|4|3|La Peau du chagrin|1831|Honoré|de Balzac|

## 5

|book_id|author_id|title|year|firstname|lastname|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|3|Les Illusions perdues|1837|Honoré|de Balzac|
|2|3|Mémoires d'outre-tombe|1849|François-René|de Chateaubriand|
|3|4|Le Petit chose|1868|NNULL|NULL|
|4|3|La Peau du chagrin|1831|Honoré|de Balzac|

## 6

|book_id|author_id|title|year|firstname|lastname|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|3|Les Illusions perdues|1837|Victor|Hugo|
|2|3|Mémoires d'outre-tombe|1849|François-René|de Chateaubriand|
|4|3|La Peau du chagrin|1831|Honoré|de Balzac|
|NULL|2|NULL|NULL|Victor|Hugo|

## 7

|book_id|author_id|title|year|firstname|lastname|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|3|Les Illusions perdues|1837|Victor|Hugo|
|2|3|Mémoires d'outre-tombe|1849|François-René|de Chateaubriand|
|3|4|Le Petit chose|1868|NULL|NULL|
|4|3|La Peau du chagrin|1831|Honoré|de Balzac|
|NULL|2|NULL|NULL|Victor|Hugo|

## 8

```sql
SELECT *
FROM library.books
    LEFT JOIN library.authors USING (author_id)
UNION
SELECT *
FROM library.books
    RIGHT JOIN library.authors USING (author_id)
```
|
## 9

```sql
SELECT *
FROM library.books
    LEFT JOIN library.authors USING (author_id)
INTERSECT
SELECT *
FROM library.books
    RIGHT JOIN library.authors USING (author_id)
```

## 10

```sql
SELECT *
FROM library.books
NATURAL JOIN library.authors
```
> Non le seul problèmes est de suivre les convention de nommage de SQL mais ce n'est pas un problème important parce que même sans la commande `NATURAL JOIN` les convention doivent être suivies quand même

# Recherche d'un *extremum*

## 1

3200

## 2

### 1

|competitors_id|name|country|score|competitors_id|name|country|score|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|Tux|LX|3200|NULL|NULL|NULL|NULL|
|2|Linus|LX|3200|NULL|NULL|NULL|NULL|
|3|Bill|US|150|5|Steve|US|399|
|3|Bill|US|150|1|Tux|LX|3200|
|3|Bill|US|150|2|Linus|LX|3200|
|4|Boule|US|150|5|Steve|US|399|
|4|Boule|US|150|1|Tux|LX|3200|
|4|Boule|US|150|2|Linus|LX|3200|
|5|Steve|US|399|1|Tux|LX|3200|
|5|Steve|US|399|2|Linus|LX|3200|

### 2

> Sa solution fonctionne car les seules avec des `NULL` sont ceux qui on le plus de points.

# Requêtes

## 1

```sql
SELECT *
FROM library.books AS l, library.authors AS a 
WHERE l.author_id = a.author_id
AND a.firstname = 'Honoré'
AND a.lastname = 'de Balzac'
```

## 2

```sql
SELECT *
FROM library.books
WHERE year >= 1825
AND year <= 1835
```

## 3

```sql
SELECT *
FROM library.books AS l, library.authors AS a
WHERE year IS NOT BETWEEN 1825 AND 1835
AND l.author_id = a.author_id
AND a.firstname = 'Honoré'
AND a.lastname = 'de Balzac'
```

## 4

```sql
SELECT a.firstname, a.lastname, COUNT(book_id)
FROM library.books l
LEFT JOIN library.authors USING (author_id)
GROUP BY author_id
```
