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
    num_etu SERIAL PRIMARY KEY,
    prénom TEXT NOT NULL,
    nom TEXT NOT NULL
);

CREATE TABLE module (
    code_alpha TEXT PRIMARY KEY,
    nom TEXT NOT NULL,
);

CREATE TABLE evalué (
    num_etu SERIAL REFERENCES Étudiant(num_etu),
    code_alpha TEXT REFERENCES module(func_id),
    note INT,
    
    PRIMARY KEY(num_etu, code_alpha)
);
```

# Exercice 7

```sql
CREATE TABLE Pays (
    id_pays SERIAL PRIMARY KEY,
    nom TEXT NOT NULL,
    monnaie TEXT NOT NULL
);

CREATE TABLE Régions (
    id_régions SERIAL PRIMARY KEY,
    nom TEXT NOT NULL,
    langue TEXT NOT NULL,
    id_pays SERIAL REFERENCES Pays(id_pays)
);
```

# Exercice 8

```sql
```
