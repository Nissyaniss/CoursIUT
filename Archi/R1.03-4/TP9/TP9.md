# Exercice 1

```bash
if (($# != 1))
then
	echo "Il faut un argument" >&2
	exit 1
fi

if [ -x $1 ] || [ ! -f $1 ]
then
	echo "Le fichier est un executable" >&2
	exit 1
fi

i=1
IFS=$'\n'
for line in $(cat $1)
do
	echo "$i $line"
	if ((i % 20 == 0))
	then
		read -p "Suite o/n: " choice
		if [ $choice != "o" ]
		then
			exit 0
		fi
	fi
	((i += 1))
done
```

# Exercice 2

```bash
if (($# != 1))
then
	echo "Il faut un argument." >&2
	exit 1
fi

if [ ! -f $1 ]
then
	echo "Il faut un fichier." >&2
	exit 1
fi

for line in $(cat $1)
do
	temp=$(echo "$line" | cut -d':' -f2 | tr -d " " | tr ";" ",")
	$(echo "$line" | grep "\." >/dev/null)
	if (($? == 0))
	then
		temp=$(echo "$line" | tr -d ".")
		echo "$temp" >> result.csv
	else
		echo -n "$temp" >> result.csv
	fi
done
```