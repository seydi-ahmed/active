# ACTIVE

## Description:
Ce projet est un simple scanner de ports TCP et UDP en Python. Il permet de vérifier si un port est ouvert ou fermé, et affiche le nom du service associé s'il est disponible.

## Explication du code:
1) Options: Le programme supporte les scans TCP (-t), les scans UDP (-u), et une option d'aide (--help).
2) Plage de ports: Vous pouvez spécifier une plage de ports avec l'option -p (par exemple, 80 ou 80-85).
3) Services: Le programme affiche également le nom du service associé au port ouvert, en utilisant socket.getservbyport() pour récupérer les services standards (HTTP, FTP, etc.).
4) UDP ne garantit pas la réception d'une réponse comme TCP, c'est pourquoi le scanner ne peut pas toujours conclure que le port est ouvert s'il ne reçoit pas de réponse. En envoyant une réponse (ACK), vous permettez au scanner de vérifier que le port est bien ouvert.

## Installation:
- git clone https://learn.zone01dakar.sn/git/mouhameddiouf/active.git

## Utilisation:
### HELP:
- Exécuter la commande ```python3 tinyscanner.py help```
### TCP:
- Exécuter le programme ```tcp_server.py``` avec le port de votre choix
- puis éxécuter cette commande ```python3 tinyscanner.py -t 127.0.0.1 -p port```
### UDP:
- Exécuter le programme ```udp_server.py``` avec le port de votre choix
- puis éxécuter cette commande ```python3 tinyscanner.py -u 127.0.0.1 -p port```

## Développeur:
- NOM Prénom: DIOUF Mouhamed
- Email: Seydiahmedelcheikh@gmail.com
- git: mouhameddiouf