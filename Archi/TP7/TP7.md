# 1

```bash
# !/bin/bash

echo "Nb d'arguments $#"
echo $1
echo $2
echo $3
echo "Arguments : \$*" $*
```

1)
```text
Nb d'arguments 3
bonjour
à
tous
Arguments : $* bonjour à tous
```

2)
> D'afficher le nombre d'arguments passés au script

3)
```bash
# !/bin/bash

echo "Nb d'arguments $#"
echo $3
echo $4
echo $5
echo "Arguments : \$*" $*
```

# 2

```bash
i=5
echo $((i = i + 8))
((i = i + 5))
echo $i
echo $((5 > 12))
((5 > 12))
echo $?
```

```text
13
18
0
1
```

# 3

```bash
# !/bin/bash

test -d $1
```

# 4

```bash
# !/bin/bash

if (( $1 > 10 && $1 > 100))
then
	echo "Entier $1 supérieur à 100"
elif (( $1 < 10 ))
then
	echo "Entier $1 inférieur à 10"
elif (( $1 > 10 ))
then
	echo "Entier $1 supérieur à 10 mais inférieur à 100"
fi
```

# 5

```bash
# !/bin/bash

if (( $# == 1 ))
then
	echo "Il y a un seul argument"
else
	echo "Il y a plus ou moins d'un argument"
fi
```

```bash
# !/bin/bash

if (( $# == 1 ))
then
	echo "Il y a un seul argument"
elif (( $# == 0 ))
then
	echo "Il n'y a pas d'arguments"
else
	echo "Il y a plus ou moins d'un argument"
fi
```

# 6

```bash
# !/bin/bash

if (( $# != 2 ))
then
	echo "Le nombre d'arguments est incorrect" >&2
	exit 1
fi

if (( $1 > $2 ))
then
	echo "La plus grande valeur est $1"
else
	echo "La plus grande valeur est $2"
fi

```

# 7

```bash
# !/bin/bash

if (( $# != 1 ))
then
	echo "Le nombre d'arguments est incorrect" >&2
	exit 1
fi

echo $1 | cut -d: -f3
```

# 8

```bash
# !/bin/bash

if (( $# != 1 ))
then
	echo "JE RÉCLAME SEULEMENT 1 ARGUMENT" >&2
	exit 1
fi
grep ^$1: /etc/passwd >/dev/null 2>/dev/null

if (( $? != 0 ))
then
	echo "VOTRE NOM N'EST PAS DANS /etc/passwd"
else
	echo "WOW VOTRE NOM EST DANS /etc/passwd"
fi
```

# 9

```bash
# !/bin/bash

echo "Entrez la largeur"
read largeur
if ((largeur == 0 ))
then
	echo "Largeur ne peut pas être égual à 0" >&2
	exit 1
fi
echo "Entrez la longueur"
read longueur
if ((longueur == 0 ))
then
	echo "Longueur ne peut pas être égual à 0" >&2
	exit 1
fi
if ((largeur > longueur ))
then
	echo "Largeur ne peut pas être supérieur à la longueur" >&2
	exit 1
fi

echo "L'aire du rectangle est $((largeur * longueur))"
```