# Exercice 1

## 1

> R1, PCA, PCB -> 172.16.12.3/24 -> 172.16.12.0/24, passerelle : R1(eth3)\
> R1, Internet -> 123.45.0.0/22, passerelle : R1(eth0)\
> R1, R2 -> 10.0.5.0/28, pas de passerelle car 2 routeurs\
> R1, R3 -> 10.0.0.0/28, pas de passerelle car 2 routeurs\
> R4, PCE -> 172.16.20.0/24, passerelle : R4(eth2)\
> R2, PCC, PCD, HTTP -> 172.16.17.0/24, passerelle : R2(eth2)\
> R3, DNS, R4 -> 172.16.15.0/24, passerelle : R3(eth2) (Mieux parce que on peux se connecter a interbet) ou R4(eth1)

## 2

### 1

|+ CMD|- CMD|+ Pérenne|- Pérenne|
|:-:|:-:|:-:|:-:|
|C'est rapide et facile|Perte dés arrêt du PC|Pas de perte au démarrage|NULL|
|NULL|Perte car override par un autre programme|NULL|Perte de fichier|

### 2

#### 1

> `/etc/network/interfaces`

#### 2

```text
auto lo
iface lo inet loopback

auto eth1
iface eth1 inet static
address 10.0.5.2
netmask 255.255.255.240
gateway 10.0.5.1

auto eth2
iface eth2 inet static
address 176.16.17.254
netmask 255.255.255.0
gateway 10.0.5.1
```

## 3

### 1

> 172.16.17.0/24, donc HTTP a 172.16.17.1/24

### 2

#### 1

> PCA -> R1 -> R2 -> HTTP

#### 2

> PCA (ok car R1 passerelle) -> R1 (nok car R1 n'a pas d'interface sur le réseau de HTTP et pas de route configurée) -> R2 -> HTTP\
> Le paquet est détruit car cela ne marche pas.

#### 3

`ip route add 172.16.17.0/24 via 10.0.5.2` (sur R1)\
`ip route add default via 172.16.17.254`(sur HTTP)\
`ip route add 172.16.12.0/24 via 10.0.5.1` (sur R2)

## 4

### 1

> DNS

### 2

> Il faut configurer sur PCA un serveur DNS.\
> Dans le fichier : /etc/resolv.conf\
> On ajoute :
```
nameserver 172.16.15.5
```

### 3

> PCA interroge le DNS pour récupérer @IP de bleu.org\
> DNS répond avec @IP\
> PCA peut envoyer sa requête\
> PCA -> R1 -x> R3 -> DNS

### 4

> `ping eth3`(sur PCA) -> OK\
> `ping 10.0.0.2(eth1)`(sur PCA) -> NOK\
> `ping 172.16.15.5` (sur R1) -> NOK

### 5

> `ip route add 172.16.15.0/24 via 10.0.0.2`\
> `ip route add 172.16.15.0/24 via 10.0.0.1`

## 5

> Sur R1 -> `ping 8.8.8.8` -> OK car R1 connecté a internet\
> Sur PCA -> `ping 8.8.8.8` -> NOK car l'adresse de PCA est local car 172 (ou 192) est local

# Exercice 2

> Protocole Utilisé : TCP, HTTP, DNS\
> Adresses et protocole : 145.254.160.237:3372 -> 65.208.228.223:80 TCP, 145.254.160.237:?? -> 145.253.2.203:53(Port Standard DNS) DNS, 145.254.160.237 -> 216.239.59.99:53(Port Standard HTTP) HTTP\
|TCP|HTTP|DNS|
|:-:|:-:|:-:|
|65.208.228.223|65.208.228.223, 216.239.59.99|145.253.2.203|
> Lignes 1 à 3 -> Établissement de la connexion TCP par handshake parce que [SYN] -> [SYN, ACK] -> [SYN]\
> Ligne 4 -> 145.254.160.237 demande à 65.208.228.223 la page download.html par protocole HTTP\
> Lignes 5 à 12 -> Chargement de la page\
> Ligne 13 -> 145.254.160.237 demande l'IP de pagead2.googlesyndication.com à 145.253.2.203\
> Ligne 17 -> Réponse DNS
> Ligne 18 -> 145.254.160.237 demande /pagead/... a 216.239.59.99
