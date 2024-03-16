# Exercice 1

## 1

> Réseaux 1: 192.168.5.0/24, PCA, PCB, R1 sur eth2\
> Réseaux 2: 10.0.0.0/8, R1 sur eth0, R2 sur eth1\
> Réseaux 3: 172.31.0.0/16, R2 sur eth2, PCF\
> Réseaux 4: 172.16.0.0/16, R2 sur eth0\
> Réseaux 5: 134.56.0.0/16, R1 sur eth1

## 2

### 1

```bash
ping 192.168.5.43
```

### 2

> Ca marche.

### 3

> Ping 1:
>> Expéditeur IP : 192.168.5.1\
>> Expéditeur MAC : a6:65:ab:d8:d5:f1\
>> Destinataire IP : 192.168.5.43\
>> Destinataire MAC : 42:49:e3:f4:10:92\
> Ping 2:
>> Expéditeur IP : 192.168.5.43\
>> Expéditeur MAC : 42:49:e3:f4:10:92\
>> Destinataire IP : 192.168.5.1\
>> Destinataire MAC : a6:65:ab:d8:d5:f1

### 4

> Un requête pour l'adresse MAC de PCB de la part de PCA, et une réponse de PCB ou de R1 si il l'a de stocké.

## 3

> Le ping ne réussira pas car ils ne sont pas dans le même réseaux.

## 4

```bash
ip route add default via 192.168.5.254
```

## 5

```bash
ip route show
```

# Exercice 2

## 1

Ping request
|||
|:-:|:-:|
|PCA -> R1|Route mise en place|
|R1 -> R2|Route manquante|
|R2 -> PCF|Route mise en place|

Ping réponse
|||
|:-:|:-:|
|PCF -> R2|Route mise en place|
|R2 -> R1|Route manquante|
|R1 -> PCA|Route mise en place|

## 2

```bash
ip route add 172.31.0.0/16 via 10.0.0.2
ip route add 192.168.5.0/24 via 10.0.0.1
```

## 3

> Ping request
>> PCA IP : 192.168.5.1\
>> PCA MAC : a6:65:ab:d8:d5:f1\
>> R1 IP : 192.168.5.254\
>> R1 MAC : 7d:94:1e:8c:4a:4b\
> Ping request
>> R1 IP : @R1 eth0\
>> R1 MAC : @R1 eth0\
>> R2 IP : @R2 eth1\
>> R2 MAC : @R2 eth1\
> Ping request
>> R2 IP : @R2 eth2\
>> R2 MAC : @R1 eth2\
>> PCF IP : @PCF\
>> PCF MAC : @PCF\
> Ping réponse
>> PCF IP : @PCF\
>> PCF MAC : @PCF\
>> R2 IP : @R2 eth2\
>> R2 MAC : @R2 eth2\
> Ping request
>> R2 IP : @R2 eth1\
>> R2 MAC : @R2 eth1\
>> R1 IP : @R1 eth0\
>> R1 MAC : @R1 eth0\
> Ping request
>> R1 IP : @R1 eth2\
>> R1 MAC : @R1 eth2\
>> PCA IP : @PCF\
>> PCA MAC : @PCF

## 4

Sur R1 :
```bash
ip route add 172.16.0.0/16 via 10.0.0.2
```
Sur la machine destination :
```bash
ip route add default via 172.16.0.1
```

# Exercice 3

## 1

> 164.81.20.0, 192.168.12.0, 10.25.0.0, 127.0.0.0

## 2

> ??

## 3

|IP destinataire|Passerelle|
|:-:|:-:|
|19.25.54.7|164.81.20.254?|
|192.168.11.23|192.168.12.254|
|172.29.23.1|192.168.12.254|
|10.23.34.56|164.81.20.254??|

## 4

> La passerelle par défaut de M est 164.81.20.254

## 5

### 1

> Non ce n'est pas assuré car la ligne "192.168.11.0 255.255.255.0 192.168.12.254" indique déjà le chemin a prendre.

### 2

```bash
ip route add 192.168.11.23/32 via 10.25.0.254
```
