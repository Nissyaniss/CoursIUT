# 1 - Utilitaires

## head

> Syntaxe : `head [OPTION]... [FICHIER]...`
```bash
$ head -5 fic

clavier 102 touches:500:1
hard disk:5000:18
imprimante Epson:5600:0
ecran vga:4680:30
clavier 82 touches:900:0

$ head fic

clavier 102 touches:500:1
hard disk:5000:18
imprimante Epson:5600:0
ecran vga:4680:30
clavier 82 touches:900:0

$ cat fic | head -3

clavier 102 touches:500:1
hard disk:5000:18
imprimante Epson:5600:0
```

## tail

> Syntaxe : `tail [OPTION]... [FICHIER]...`

```bash
$ tail -2 fic

ecran vga:4680:30
clavier 82 touches:900:0

$ tail -n +2 fic

hard disk:5000:18
imprimante Epson:5600:0
ecran vga:4680:30
clavier 82 touches:900:0

$ head -3 fic | tail -1

imprimante Epson:5600:0

$ head -3 fic | tail -n +2

clavier 102 touches:500:1
hard disk:5000:18
imprimante Epson:5600:0
```

## cut

> Syntaxe : `cut [OPTION]... [FICHIER]...`

```bash
$ cut -c1-2,3 fic

cla
har
imp
ecr
cla

$ head -1 fic | cut -c1-2,3

cla

$ cut -d':' -f1,3 fic

clavier 102 touches:1
hard disk:18
imprimante Epson:0
ecran vga:30
clavier 82 touches:0

$ tail -1 fic | cut -d':' -f1

clavier 82 touches
```

## tr

> Syntaxe : `tr [OPTION]... [CHAINE1] [CHAINE2]`

```bash
$ cat fic | tr '[a-z]' '[A-Z]'

CLAVIER 102 TOUCHES:500:1
HARD DISK:5000:18
IMPRIMANTE EPSON:5600:0
ECRAN VGA:4680:30
CLAVIER 82 TOUCHES:900:0

$ head -1 fic | tr -d ' '

clavier102touches:500:1

$ head -2 fic | tail -1 | tr -s ' ' '_'

hard_disk:5000:18
```

## wc

> Syntaxe : `wc [OPTION]... [FICHIER]...`

```bash
$ wc -1 fic

5

$ tail -n +2 fic | wc -1

4

```

## Test sur machine

### b

```bash
$ cut -d':' fic -f2

$ cat fic | tr -s ':' ' '

$ cat fic | tr -s ':' '\n'
```

## sort

> Syntaxe : `sort [OPTION]... [FICHIER]...`

```bash
$ sort -t':' fic

clavier 102 touches:500:1
clavier 82 touches:900:0
ecran vga:4680:30
hard disk:5000:18
imprimante Epson:5600:0

$ sort -t':' -r fic

imprimante Epson:5600:0
hard disk:5000:18
ecran vga:4680:30
clavier 82 touches:900:0
clavier 102 touches:500:1

$ sort -t':' -k2 fic

ecran vga:4680:30
hard disk:5000:18
clavier 102 touches:500:1
imprimante Epson:5600:0
clavier 82 touches:900:0

$ sort -t':' -n -k3 fic

clavier 82 touches:900:0
imprimante Epson:5600:0
clavier 102 touches:500:1
hard disk:5000:18
ecran vga:4680:30

$ sort -t':' -n -k2 fic | tail -1 | cut -d':' -f1

imprimante Epson

$ sort -t':' -n -k2 fic | head -1 | cut -d':' -f1

clavier 102 touches
```