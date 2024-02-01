# Partie 1

## Exercice 1

```bash
$ echo $a
pwd

$ echo '$a'
$a

$ echo "$a"
pwd

$ echo `$a`
/home/nissya
```

## Exercice 2

```bash
$ a=il était une fois
zsh: command not found: était
```

> La commande correcte aurait été :
```bash
$ a='il était une fois'
```

## Exercice 3

```bash
$ echo $b$a
il étaitune fois
$ echo $b $a
il était une fois
$ echo $b' '$a
il était une fois
$ echo $b" "$a
il était une fois
$ echo '$b $a'
$b $a
$ echo "$b $a"
il était une fois
```

## Exercice 4

```bash
$ a=xy;echo $a
xy

$ b=$xy;echo $b

$ c=$x$y$x;echo $c
abcdefabc

$ d=${x}y;echo $d
abcy

$ e=t$xy;echo $e
t

$ f=t${x}y;echo $f
tabc

$ g=t${x}$y;echo $g
tabcdef
```

## Exercice 5

```bash
$ a='pwd';echo $a
pwd

$ a="pwd";echo $a
pwd

$ a=`pwd`;echo $a
/home/nissya

$ a=`pwd`;echo '$a'
$a

$ a="pwd";echo "$a"
/home/nissya

$ a=pwd;echo $a
pwd

$ a=pwd;echo `$a`
/home/nissya

$ echo Mon répertoire courant est `pwd`
Mon répertoire courant est /home/nissya

$ echo 'Mon répertoire courant est `pwd`'
Mon répertoire courant est `pwd`

$ echo "Mon répertoire courant est `pwd`"
Mon répertoire courant est /home/nissya
```

## Exercice 6

> La différence entre `$ echo toto ; echo toto` et `$ echo toto ';' echo toto` est l'affichage car elles vont respectivement afficher `toto ; echo toto` et 
> ```bash
> toto
> toto
> ```

> Pour afficher 'echo toto ';'echo toto'

```bash
$ echo "echo toto ';' echo toto"
echo toto ; echo toto
```

## Exercice 7

```bash
$ echo '\\'
\

$ echo "\\"
\

$ echo \$a
$a

$ echo '"'
"

$ echo *
/home/nissya (exemple hein)

$ echo '*'
*

$ echo \\
\

$ echo \"\'
"'

$ echo "\$a"
$a

$ echo "'"
'

$ echo \*
*

echo "*"
*
```

## Exercice 8

```bash
$ echo '$HOME'

$ echo "\$HOME"
```

## Exercice 9

```bash
$ a=salut
$ echo $a
salut
$ bash
$ echo $a

$ a=bonjour
$ echo $a
bonjour
^D
$ echo $a
salut
$ export a
$ bash
$ echo $a
salut
$ a=bonjour
$ echo $a
bonjour
^D
$ echo $a
salut
```

# Partie 2

## Exercice 1

```bash
$ ls
(ls)

$ echo $?
0

$ ls zzaaer
Error

$ echo $?
2
```

## Exercice 2

```bash
$ >toto
(créer le fichier 'toto')

$ cat toto

$ echo $?
0

$ cat rien
Error

$ echo $?
1

$ echo $?
0
```

## Exercice 3

```bash
$ cat fic && echo TROUVE
(fic)
TROUVE

$ cat fic || echo "PAS TROUVE"
(fic)

$ cat toto || echo "PAS TROUVE"
Error cat
PAS TROUVE

$ cat toto ; echo "TROUVE"
Error cat
TROUVE

$ cat toto || echo "PAS TROUVE" >/dev/null
Error cat

$ (cat toto || echo "PAS TROUVE") >/dev/null
Error cat

$ cat toto || echo "PAS TROUVE" >/dev/null 2>/dev/null
Error cat
```

## Exercice 4

(Voir yestu)