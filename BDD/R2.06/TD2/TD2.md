# Exercice 1

```sql
CREATE SCHÉMA BLOG
CREATE TYPE blog.STATUS AS ENUM('brouillon', 'publié', 'en attente');

CREATE TABLE blog.articles (
    article_id SERIAL PRIMARY KEY,
    status blog.STATUS NOT NULL
);
```

# Exercice 2

```sql
CREATE SCHÉMA BLOG
CREATE TYPE blog.STATUS AS ENUM('brouillon', 'publié', 'en attente');

CREATE TABLE blog.articles (
    article_id SERIAL PRIMARY KEY,
    status blog.STATUS
);
```

# Exercice 3

```sql
CREATE SCHÉMA BLOG
CREATE TYPE blog.STATUS AS ENUM('brouillon', 'publié', 'en attente');

CREATE TABLE blog.articles (
    article_id SERIAL PRIMARY KEY,
    titre TEXT NOT NULL,
    corps TEXT NOT NULL,
    autheur_id INT NOT NULL REFERENCES blog.autheur(author_id),
    status blog.STATUS
);

CREATE TABLE blog.autheur (
    autheur_id INT NOT NULL,
    nom TEXT NOT NULL
);
```

# Exercice 4

```sql
CREATE SCHÉMA BLOG
CREATE TYPE blog.STATUS AS ENUM('brouillon', 'publié', 'en attente');

CREATE TABLE blog.articles (
    article_id SERIAL PRIMARY KEY,
    titre TEXT NOT NULL,
    corps TEXT NOT NULL,
    autheur_id INT NOT NULL REFERENCES blog.autheur(author_id),
    status blog.STATUS
);

CREATE TABLE blog.autheur (
    autheur_id INT NOT NULL,
    nom TEXT NOT NULL
);

CREATE TABLE blog.multAutheur (
    autheur_id INT NOT NULL REFERENCES blog.auteur(autheur_id)
        ON DELETE CASCADE,
    article INT NOT NULL REFERENCES blog.article(article_id)
        ON DELETE CASCADE,
    PRIMARY KEY (auteur, article)
);
```

# Exercice 5

```sql
CREATE TABLE Dev (
    dev_id SERIAL PRIMARY KEY,
    nom TEXT NOT NULL,
    prénom TEXT NOT NULL,
);

CREATE TABLE Fonctionnalité (
    func_id SERIAL PRIMARY KEY,
    titre TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE works_on (
    dev_id INT NOT NULL REFERENCES Dev(dev_id)
        ON DELETE CASCADE,
    func_id INT NOT NULL REFERENCES Fonctionnalité(func_id)
        ON DELETE CASCADE,
    DateDébut DATE NOT NULL,
    DateFin DATE NOT NULL

    PRIMARY KEY (dev_id, func_id)
);
```

# Exercice 6

```sql
CREATE TABLE Étudiant (
    num_etu TEXT PRIMARY KEY,
    prénom TEXT NOT NULL,
    nom TEXT NOT NULL
);

CREATE TABLE module (
    code_alpha TEXT PRIMARY KEY,
    nom TEXT NOT NULL,
);

CREATE TABLE evalué (
    num_etu TEXT REFERENCES Étudiant(num_etu) NOT NULL,
        ON UPDATE CASCADE ON DELETE CASCADE
    code_alpha TEXT REFERENCES module(func_id),
        ON UPDATE CASCADE ON DELETE CASCADE
    note INT,
    
    PRIMARY KEY(num_etu, code_alpha)
);
```

# Exercice 7

```sql
CREATE TABLE Pays (
    nom TEXT PRIMARY KEY NOT NULL,
    monnaie TEXT NOT NULL
);

CREATE TABLE Régions (
    nom TEXT NOT NULL,
    langue TEXT NOT NULL,
    nom TEXT REFERENCES Pays(nom)
        ON UPDATE CASCADE ON DELETE CASCADE
);
```

# Exercice 8

```sql
CREATE SCHEMA ville;

CREATE TABLE ville.Immeuble (
    id_immeuble SERIAL PRIMARY KEY,
    nom TEXT NOT NULL,
    adresse TEXT NOT NULL,
);

CREATE TABLE ville.Propriétaire (
    id_propriétaire SERIAL PRIMARY KEY
);

CREATE TABLE ville.Appartement (
    numéro INT NOT NULL,
    propriétaire INT REFERENCES ville.Propriétaire (id_proprio)
        ON DELETE SET NULL,
    id_immeuble INT REFERENCES ville.Immeuble (id_immeuble) NOT NULL
        ON DELETE CASCADE

    PRIMARY KEY(id_immeuble, numéro)
);
```

# Exercice 9

```sql
CREATE TABLE Véhicule (
    idVéhicule SERIAL NOT NULL,
    modèle TEXT NOT NULL,
    prix DECIMAL NOT NULL
);

CREATE TABLE Véhicule_a_moteur (
    idVéhicule INT REFRENCES Véhicule(idVéhicule)
        ON DELETE CASCADE PRIMARY KEY,
    puissance INT NOT NULL
);

CREATE TABLE Vélo (
    idVéhicule INT REFERENCES Véhicule(idVéhicule)
        ON DELETE CASCADE PRIMARY KEY
);
```

# Exercice 10

```sql
CREATE SCHEMA Forum;

CREATE TABLE Utilisateur (
    id_utilisateur SERIAL PRIMARY KEY,
    nom TEXT NOT NULL,
    prénom TEXT NOT NULL
);

CREATE TABLE Message (
    id_mess SERIAL PRIMARY KEY,
    contenu TEXT NOT NULL
)

CREATE TABLE Réponse (
    id_mess INT REFERENCE Message(id_mess) PRIMARY KEY,
    message INT REFERENCE Message(id_mess),
)

CREATE TABLE OuvreFil (
    id_mess INT REFENCES Message(id_mess) PRIMARY KEY,
    Titre TEXT NOT NULL
)
```
