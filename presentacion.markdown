% LibreVPN
% Una red libre virtual
% librevpn.org.ar

Un proyecto de...
=================

---

![](assets/img/LogoHacklab.svg)

---

## Bajo licencia AGPLv3

![](assets/img/AGPLv3_Logo.svg)


Cómo se ve
==========

---

<iframe class="stretch force" src="force_falso.html"></iframe>

---

## En realidad ahora mismo se ve así

---

<iframe class="stretch force" src="force.html"></iframe>

Qué no es
=========

---

Un túnel para proteger el tráfico

Para eso está RiseUp.net!  Pero es posible, si alguien te deja


Qué es
======

---

## Una red en malla

Cada nodo es cliente y servidor a la vez

Y se puede conectar con otros sin pasar por un servidor central

(aunque si no hay conexión directa, se delega el tráfico)

## Una caja de herramientas para crear VPNs

---

`lvpn` es una serie de herramientas para crear nodos, correr comandos
personalizados en eventos de la red, auto asignar direcciones IP y rutas
por defecto, etc.


why!
====

---

![](assets/img/annoyed-y-u-no.svg)

---

Internet no funciona como una red de pares, algunos son servidores y la
mayoría son clientes

---

Hay cosas que no funcionan en Internet gracias a las NAT: la mayoría de
las máquinas no tienen una IP pública.

---

Aunque quisiéramos, los proveedores de Internet bloquean puertos o
te cambian la IP

(alguien probó tener un servidor de correo en casa?)

---

Hay segmentos de redes libres que no se ven entre sí

(no te respondió el ping!)

---

## Entonces

Necesitamos una red que supere estos problemas, no tener que reinventar
servicios que esquiven los problemas de la Internet actual.


## En realidad

Nos gusta jugar con el grafo (miren cómo se mueve!)


Cosas piolas
============

---

* El tráfico es cifrado
* Ningún puerto bloqueado
* Los nodos no son terminales
* Funciona en Android y en OpenWrt
* Multicast funciona!
* IPv6 nativo!

---

## IPv6 nativo!

---

Cada nodo tiene una IPv6 en el rango `2001:1291:200:83ab::/64`

18.446.744.073.709.551.616 de nodos posibles

---

## Qué quiere decir?

---

Que cada nodo es un nodo de la Internet del futuro

![](assets/img/logo-top.png)

---

Una red adentro de otra!! Primero por Internet4, luego por LibreVPN y
luego por Internet6.

Otras VPNs usan rangos privados: `fe80::`


# Qué onda, cómo le hacen

---

La red se levanta con **tinc**, usamos **avahi** para descubrimiento de
servicios y mDNS y **lvpn** para configurar.


## Crear un nodo

---

En una máquina

    lvpn init -i un_nodo
    tincd -n lvpn
    lvpn announce

---

En otra

    lvpn init -i otro_nodo
    tincd -n lvpn
    lvpn discover

    ping un_nodo.local
    ping6 un_nodo.local

---

Todo esto dentro de una red local


# Cosas copadas para hacer

---

Cualquier servicio que funcione en una LAN funciona en LibreVPN...

## Chat sin servidores

Creá una cuenta Bonjour en Pidgin o Empathy

---

## Red IRC

irc.hackcoop.com.ar también es... 192.168.9.3

o [2001:1291:200:83ab:249a:2ef4:9cad:1d9e]

o **naven.local**

o _exodica.local_ (y sus IPs)

---

## Directorios compartidos

FTP, SMB, AFP, BitTorrent, GlusterFS...

---

## Correo distribuido

http://wiki.hackcoop.com.ar/Correo\_distribuido

---

![](assets/img/Correo_distribuido_vectorizado.svg)

---

## Correo local

http://wiki.hackcoop.com.ar/Correo\_local

---

## Y más!

---

## OWNS

DNS distribuido

https://github.com/fauno/owns

---

![](assets/img/owns.svg)


# Quiero participar!

---

## Create un nodo!

(ya viste cómo)

---

## Cosas para hacer

(o terminar)

---

* Enlazar más! (al menos tres enlaces por nodo)
* Cada nodo un nodo público (owns, nat-pmp)
* Intercambio de llaves por Internet (usando tor?)
* Rutear entre varias redes (otras vpns o redes libres)
* Convertir cada nodo en un router de su red (radvd)
* Probar protocolos de ruteo dinámico más avanzado (babeld)
* Una GUI?


# Listo

## A galponear!

![](assets/img/Galponzin.png)

http://wiki.hackcoop.com.ar/Galponeo

---

### librevpn.org.ar<br /><small>/presentacion.html</small>

**Lista**
:   vpn@hackcoop.com.ar

**fauno**
:   fauno@endefensadelsl.org
:   0x456032D717A4CD9C

**Licencia de Producción de Pares**
:   ![](assets/img/nc.png)
:   Esta presentación se libera bajo la PPL
:   http://endefensadelsl.org/ppl\_deed\_es.html
