# Question 1

```bash
a=10
while (( $a > 0 ))
do
	((a = $a - 1))
	echo "J'ai enlevé un et var vaut " $a
done
```

```bash
for i in $(seq 9 -1 0)
do
	echo "J'ai enlevé un et var vaut " $i
done
```

# Question 2

```bash
echo "Saisir le nombre: "
read nb
for i in $(seq 0 $(($nb - 1)))
do
	((result = $result + i))
done
echo "La somme des 45 premiers entiers est:" $result
```

# Question 3

```bash
if (($# != 1))
then
	echo "Pas assez d'arguments"
	exit 1
fi
for path in $(echo $PATH | tr : '\n')
do
	if [ -f "$path/$1" ]
	then
		echo $path/$1
		exit 0
	fi
done

echo "Commande inconnue"
```

# Question 4

```bash
ls

for i in *.txt
do
	mv $i $i.old 2>/dev/null
done

ls
```

# Question 5

```bash
if (($# != 0))
then
	echo "Trop d'arguments"
fi
for i in $(who | cut -d' ' -f1,4 | tr ' ' ,)
do
	echo $(echo $i | cut -d, -f1) "est connecté sur" $(echo $i | cut -d, -f2) avec les droits $(stat /dev/$(echo $i | cut -d, -f2) --printf=%A)
done
```

# Question 6

```bash
if (($# != 1))
then
	echo "Mauvais nombre de paramètres"
	exit 1
fi

if [ ! -f "$1" ]
then
	echo "Pas un fichier"
	exit 1
fi

if [ ! -f "fic.txt" ]
then
	touch fic.txt
	for i in $(cat $1)
	do
	echo Nom: $(echo $i | cut -d, -f1)';' >>fic.txt
	echo Prénom: $(echo $i | cut -d, -f2)';' >>fic.txt
	echo Âge: $(echo $i | cut -d, -f3)';' >>fic.txt
	echo Profession: $(echo $i | cut -d, -f4)';' >>fic.txt
	echo Téléphone: $(echo $i | cut -d, -f5)';' >>fic.txt
	done
else
	a="y"
	echo "Puis-je écraser le fichier fic.txt: [y/N] "
	read a
	if [ "$a" != "y" ]
	then
		exit 0
	else
		echo -n "" >fic.txt
		for i in $(cat $1)
		do
		echo Nom: $(echo $i | cut -d, -f1)';' >>fic.txt
		echo Prénom: $(echo $i | cut -d, -f2)';' >>fic.txt
		echo Âge: $(echo $i | cut -d, -f3)';' >>fic.txt
		echo Profession: $(echo $i | cut -d, -f4)';' >>fic.txt
		echo Téléphone: $(echo $i | cut -d, -f5)';' >>fic.txt
		done
	fi
fi
```
