# Ansible Playbooks

Ansible nos permite administrar servidores de manera conjunta. Podemos lanzar comandos de forma remota a multitud de máquinas al mismo
tiempo. Mediante este conjunto de playbooks hemos sido capaces de gestionar una cantidad enorme de nodos de Cosmos. Tanto sentries como validadores.

Cuando trabajamos con Ansible es recomendable que las máquinas de nuestro inventario sean lo más homogéneas posible.

En este repositorio encontrarás playbooks para acciones simples, como subir un archivo a tus servidores. Pero también algunos más complejos, como modificar líneas concretas de archivos de configuración, instalar paquetes, reiniciar servicios etc.

Cada playbook de ansible tiene una pequeña descripción de lo que hace. Te recomendamos que revises las líneas de estos playbooks antes de utilizarlos, pues algunos de ellos son muy específicos para una situación y momento concreto en el que nos hizo falta. Sin embargo la mayoría de ellos te puede servir como base para construir tu propia librería de utilidades.

Tenemos que agradecer a @Melozo: https://github.com/melozo el gran taller introductorio a ansible que impartió en la Colmena. Nos abrió una puerta espectacular e hizo que nuestra productividad aumetara enormemente. ¡Gracias Melo!
