# ACTIVE

## Description:
Ce projet est un simple scanner de ports TCP et UDP en Python. Il permet de vérifier si un port est ouvert ou fermé, et affiche le nom du service associé s'il est disponible.

## Explication du code:
1) Options: Le programme supporte les scans TCP (-t), les scans UDP (-u), et une option d'aide (--help).
2) Plage de ports: Vous pouvez spécifier une plage de ports avec l'option -p (par exemple, 80 ou 80-85).
3) Services: Le programme affiche également le nom du service associé au port ouvert, en utilisant socket.getservbyport() pour récupérer les services standards (HTTP, FTP, etc.).

## Installation:
- git clone https://learn.zone01dakar.sn/git/mouhameddiouf/active.git

## Utilisation:

## Développeur:
- NOM Prénom: DIOUF Mouhamed
- Email: Seydiahmedelcheikh@gmail.com
- git: mouhameddiouf