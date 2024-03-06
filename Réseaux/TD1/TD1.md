# Exercice 1

## A

> Tous de classe C

## B

> (adresse)/24 255.255.255.0

## C

> 194.168.0.0/24

## D

> ip addr add 194.168.0.112/24 dev eth0

# Exercice 2

## A

> 255.255.0.0/16

## B

> 176.16.0.0/16

## C

> ip addr add 172.16.25.3/16 dev eth0

## D

> ifconfig | ipconfig

## E

> Non car il n'a pas précisé le masque et donc c'est CDIR/32 par défaut

## F

> Il ne l'a voit pas car elle n'est pas activé pour remédier a son problème il doit faire la commande `ip link set dev eth0`

## G

> Non car il n'a pas précisé le masque et donc c'est CDIR/32 par défaut

# Exercice 3

## A

> 2**(32-23) - 2 = 510 et 510 > 410

## B

### A

> 123.45.66.0/24\
> 123.45.67.0/24

### B

> 123.45.66.255\
> 123.45.67.255

### C

> 2**(32-24) - 2 = 254\
> 2**(32-24) - 2 = 254

### D

> 123.45.66.1\
> 123.45.67.1

### C

> 123.45.66.254\
> 123.45.67.254

## C

> 123.45.66.0/24\
> Utilité = Siège Social\
> 123.45.66.255\
> 254

> 123.45.67.0/25\
> Utilité = Belgique\
> 123.45.67.127\
> 126

> 123.45.67.128/25\
> Utilité = Allemagne\
> 123.45.67.255\
> 126
