# Exercice 1

## 1

172.16.17.0/24 :
- PCC
- PCD
- R2 (eth0)
172.16.12.0/24 :
- DNS
- BDD
- R1
172.16.15.0/24 :
- PCB
- DHCP
10.0.0.0/28:
- R1
- R3
10.0.5.0/28 :
- R3
- R2

## 2

R1 eth0 : 172.16.12.254
R3 eth2 : 176.16.15.254

# Exercice 2

## 1

R3

## 2

```
auto lo
iface lo inet loopback

auto eth2
iface eth2 inet dhcp
```

## 3

```
ddns-update-style none;

subnet 172.16.15.0 netmask 255.255.255.0
{
	range 172.16.15.10 172.16.15.254;
	default-lease time 21600;
	max-lease-time 43200;
	option routers 172.16.15.254;
	option domaine-name-servers 172.16.12.3;
}

host r2 {
	hardware ethernet AA:BB:CC:DD:EE:FF;
	fixed-address 176.16.15.254;
}
```

# Exercice 3

## 1

PCB -> R3 -> R2 -> HTTP
HTTP -> R2 -> R3 -> PCB

Sur PCB :
	`ip r a default via 172.16.15.254`
Sur R3 :
	`ip r a 172.16.17.0/24 via 10.0.5.2`
Sur R2 :
	`ip r a default via 10.0.5.1`
Sur HTTP:
	`ip r a default via 172.16.17.254`

## 2

BDD -> R1 -> R3 -> R2 -> HTTP
HTTP -> R2 -> R3 -> R1 -> BDD

Sur BDD :
	`ip r a default via 172.16.12.254`
Sur R1 : 
	`ip r a default via 10.0.0.2`
Sur R3 :
	`ip r a 172.16.12.0/24 via 10.0.5.2`
	`ip r a 172.16.12.0/24 via 10.0.0.1`

## 3

`/etc/resolv.conf`
`nameserver 172.16.12.3`

## 4

Requète DNS de PCB -> Réponse de DNS -> Requète de PCB vers HTTP 

## 5

C'est bon.

# Exercice 3

## 1

Le **F**ile **T**ransfer **P**rotocol est un protocole de transfert de fichiers. Pour transférer des fichiers.

## 2

`ss -lat 'dport = :67'` -> DHCP
`ss -lat 'dport = :53'` -> DNS
`ss -lat 'dport = :443'` -> HTTPS
`ss -lat 'dport = :22'` -> SSH
`ss -lat 'dport = :20'` -> FTP

## 3

Port PCB 68
Port DHCP 67

PCB envoie
DHCP recois

Sources :

Ip 0.0.0.0
Mac PCB

Destination

Ip DHCP
MAC dhcp







