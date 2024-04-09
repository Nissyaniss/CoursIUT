# Exercice 1

## 1

Réseaux 1 : R0 - PCA
Réseaux 2 : R0 - R1 - PCB
Réseaux 3 : R1 - PCC

## 2

### a

L'adresse est 192.168.2.61 car il y a 26 bit prit par le réseaux donc 1+2+4+8+16+32

### b

`ip a a 192.168.2.1 dev eth0`
`ip r a default via 192.168.2.61 dev eth0`

## 5

### b

Oui, car 25 > 0 et 25 < 62

## 6

Ca marche.

# Exercice 2

## 1

PCA : `192.168.2.1/26`
PCB : `10.0.0.1/24`
PCC : `172.16.4.1/23`
R0 IG : `192.168.2.62/26`
R0 ID : `10.0.0.254/24`
R1 IG : `10.0.0.253/24`
R1 ID : `172.16.5.254/23`

## 2

`ip a a 172.16.4.1/23 dev eth0`

## 4

Aucun

## 6

### a

`/etc/network/infarces`

## b

Son interface eth0

## c


















