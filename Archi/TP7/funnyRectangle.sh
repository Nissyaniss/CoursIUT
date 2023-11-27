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

for i in $(seq 0 $largeur)
do
	echo -n "*"
done

echo

for i in $(seq 0 $((longueur - 2)))
do
	for i in $(seq 0 $largeur)
	do
		echo -n "*"
	done
	echo
done

for i in $(seq 0 $largeur)
do
	echo -n "*"
done
echo