
# Exercice 1

## Question 1

- AP, **R1(eth0)**, client 172.16.0.0/16 (Classe B)
- **R1(eth1)**, **R2(eth0)**,DNS  192.168.10.0/24 (Classe C)
- Internet, **R0(eth0)** -> Pas d'adresse
- **R2(eth1)**, **R0(eth1)** 168.81.0.0/16 (Classe B)

## Question 2

1 et 2.
```
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
	address 172.16.10.254
	netmask 255.255.0.0
	gateway 192.168.10.254

auto eth1
iface eth1 inet static
	address 192.168.10.253
	netmask 255.255.255.0
	gateway 192.168.10.254
```

3. `/etc/resolv.conf`
```
nameserver 192.168.10.200
```

## Question 3

R1 -> R2 -> R0 -> Internet
Internet -> R0 -> R2 -> R1

Le ping s'envoie bien mais ne reviens pas car l'adresse de classe est C et seulement les classes D qui peut router sur internet.

## Question 4

`iptable -t net -A POSTROUTING -o eth1 -j MASQUERADE`

## Question 5

```
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp
```

# Exercice 2

## Question 1

1. Oui c'est possible :
		adressage static = fixe
		adressage dynamique = adresse peut changer (ex : au redémarrage de la machine)
2.  Les serveurs, les routeurs / passerelle parce que reconfiguré a chaque redémarrage devient compliqué (R0, R1, R2 et DNS)
3. `etc/dhcp/dhcpd.conf`
4. ```
```
ddns-update-style none;

subnet 172.16.0.0 netmask 255.255.0.0
{
	range 172.16.0.100 172.16.0.150;
	default-lease time 21600;
	max-lease-time 43200;
	option routers 172.16.10.254;
	option demiane-name-servers 192.168.10.200
}

subnet 192.168.10.0 netmask 255.255.255.0
{
	range 192.168.10.100 192.168.10.150;
	default-lease time 21600;
	max-lease-time 43200;
	option routers 192.168.10.254 192.168.10.254;
	option demiane-name-servers 192.168.10.200
}
```
## Question 3

DHCP :
- Pour le client port 68, protocole UDP
- Pour le serveur port 67, protocole UDP
On recherche une ligne protocole UDP et port 67 (serveur)
- J'ai rien donc mon DHCP n'est pas démarré

## Question 4

Capture A:
- Une machine sans adresse demande l'adresse du DHCP.
- Le DHCP répond une mauvaise adresse à savoir 192.168.10.100 au lieu de 192.168.10.200

Capture B:
- Mauvaise source : 172.16.10.254
- Le routeur serait 192.168.10.254 -> dans un autre domaine de collision

# Exercice 3

## Question 1

C'est la machine 192.168.10.200 qui ping 
`ping www.google.fr`

## Question 2

Client -> 192.168.10.200 port 43017
Serveur -> 164.81.1.4 port 53