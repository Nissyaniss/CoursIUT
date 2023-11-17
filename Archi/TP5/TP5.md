# Grep

## Usage

> grep [OPTION]... PATTERNS [FILE]...\
>\

### 1
> a) 
```bash
$ grep 'ecran' fic

ecran vga:4680:
```
> b)
```bash
$ grep 'ecran' fic | wc -l

1
```
> c)
```bash
$ grep -v 'ecran' fic | wc -l

5
```
> d)
```bash
$ grep 'root' example

root::0:root
bin::2:root,bin,daemon
sys::3:root,bin,sys,adm
adm::4:root,adm,daemon
mail::7:root
daemon::12:root,daemon
audit::17:root,audit
auth::21:root,auth

$ grep 'root' <example

root::0:root
bin::2:root,bin,daemon
sys::3:root,bin,sys,adm
adm::4:root,adm,daemon
mail::7:root
daemon::12:root,daemon
audit::17:root,audit
auth::21:root,auth

$ cat example | grep 'root'

root::0:root
bin::2:root,bin,daemon
sys::3:root,bin,sys,adm
adm::4:root,adm,daemon
mail::7:root
daemon::12:root,daemon
audit::17:root,audit
auth::21:root,auth
```
> e)
```bash
$ grep -v 'root' example

other::1:
uucp::5:uucp
asg::8:asg
network::10:network
sysinfo::11:sysinfo
terminal::15:
cron::16:
lp::18:lp
backup::19:
mem::20:

$ grep -c 'root' example

8

$ grep 'root' <example | wc -l

8

$ grep -c -v 'root' example

10

$ grep -cv 'root' example

10

$ grep -n 'root' example

1 root::0:root
3 bin::2:root,bin,daemon
4 sys::3:root,bin,sys,adm
5 adm::4:root,adm,daemon
7 mail::7:root
11 daemon::12:root,daemon
14 audit::17:root,audit
18 auth::21:root,auth

$ grep -nv 'root' example

2 other::1:
6 uucp::5:uucp
8 asg::8:asg
9 network::10:network
10 sysinfo::11:sysinfo
12 terminal::15:
13 cron::16:
15 lp::18:lp
16 backup::19:
17 mem::20:

$ grep '^root' example

root::0:root
```

### 2

> a)
```bash
$ grep 'imprimante' fic | wc -l
```
> b)
```bash
$ grep -i '0$' fic
```
> c)
```bash
$ grep -i ':0$' fic | wc -l
```
> d)
```bash
$ grep 'imprimante' fic | cut -d: -f2
```

### 3

> La commande `$ tail -n +2 fic | head -3 | grep '^[aeiouy]' | wc -l`\
> La première commande `tail -n +2 fic` permet de supprimer la première ligne du fichier fic.\
> La deuxième commande `head -3` permet de garder les 3 premières lignes du fichier fic.\
> La troisième commande `grep '^[aeiouy]'` permet de garder les lignes qui commencent par une voyelle.\
> La dernière commande `wc -l` permet de compter le nombre de lignes.
> Et donc elle affichera 2.

## 2

> a)
```bash
$ tail -3 fic | head -2
```
> b)
```bash
$ tail -3 fic | head -2 | cut -d: -f1
```
> c)
```bash
$ cut -d: -f3 fic | sort -nr | head -1
```
> d)
```bash
$ sort -t: -k3 -nr fic | cut -d: -f1 | head -1
```
> e)
```bash
$ cat fic | tr ':' '\n'
```
## 3

> 1)
```bash
$ head -5 /etc/passwd
```
> 2)
```bash
$ tail -5 /etc/passwd
```
> 3)
```bash
$ tail -n +2 /etc/passwd  | head -4
```
> 4)
```bash
$ tail -n +2 /etc/passwd | head -2 | tr ':' ' '
```
> 5)
```bash
$ head -10 /etc/passwd | tr a-z A-Z
```
> 6)
```bash
$ head -10 /etc/passwd | tr -d :
```

> 7)
```bash
$ head -10 /etc/passwd | cut -d: -f1 | tr a-z A-Z
```
> 8)
```bash
$ wc -l /etc/passwd
```
> 9)
```bash
$ who | wc -l
```
> 10)
```bash
$ cat /etc/passwd | cut -d: -f1,3-5 | tr ':' ' ' | sort
```
>11)
```bash
$ cat /etc/passwd | grep '^root' | tr ':' '\n'
```
> 12)
```bash
$ who | cut -d' ' -f1 | sort
```
> 13)
```bash
$ id | cut -d'(' -f2 | cut -d')' -f1
```
> 14)
```bash
$ who | head -1 | tr -s ' ' |cut -d' ' -f4
```

## Find

> 1)
```bash
$ find / -name 'find' -type f -print 2>/dev/null
```
> 2)
```bash
$ find / -name '?' -print 2>/dev/null
```
> 3)
```bash
$ find / -name '?' -print 2>/dev/null | head -1
```
> 4)
```bash
$ find / -name '*.h' -print 2>/dev/null
```
> 5)
```bash
$ find / -user nissya -type d -print 2>/dev/null 
```