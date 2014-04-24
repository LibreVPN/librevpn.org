% LibreVPN
% Una red libre virtual
% 2014-04-25

Un proyecto de...
=================

---

![](http://wiki.hackcoop.com.ar/images/9/9d/LogoHacklab.svg)


Cómo se ve
==========

---

<iframe class="force" src="force_falso.html"></iframe>

---

## En realidad ahora mismo se ve así

---

<iframe class="force" src="force.html"></iframe>

Qué no es
=========

---

Un túnel para anonimizar el tráfico (a menos que alguien te deje)


Qué es
======

---

## Una red en malla

* Cada nodo es cliente y servidor a la vez
* Y se puede conectar con los demás sin pasar por un servidor central
* Pero si no hay conexión directa, se delega el tráfico

## Una caja de herramientas para crear VPNs

---

`lvpn` es una serie de comandos para crear nodos, correr comandos
personalizados en eventos de la red, auto asignar direcciones IP y
rutas por defecto, etc.



Cosas piolas
============

---

* Ningún puerto bloqueado
* Los nodos no son terminales
* Funciona en Android
* IPv6 nativo!

---

## IPv6 nativo!

---

Cada nodo tiene una IPv6 en el rango `2001:1291:200:83ab::/64`

---

## Qué quiere decir?

---

Que cada nodo es un nodo de la Internet del futuro

---


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

Aunque cualquier servicio que funcione en una LAN funciona en
LibreVPN...

## Chat sin servidores

---

## Red IRC

---

## Correo distribuido

---

![](http://wiki.hackcoop.com.ar/images/thumb/6/6d/Correo_distribuido_vectorizado.svg/800px-Correo_distribuido_vectorizado.svg.png)

---

## Correo local

---

## Carpetas compartidas

---


# Quiero participar!

---

## Create un nodo!

---

## Cosas para hacer

---

* Cada nodo un nodo público
* Intercambio de llaves por Internet (usando tor?)
* Rutear entre varias redes (otras LibreVPN o segmentos de red)
* Convertir cada nodo en un router de su red
* Probar protocolos de ruteo dinámica más avanzado (babeld)


# Listo

---

### librevpn.org.ar

**Lista**
:   vpn@hackcoop.com.ar

**fauno**
:   fauno@endefensadelsl.org
:   0x456032D717A4CD9C
