# ACTIVE

## Description:
Ce projet est un simple scanner de ports TCP et UDP en Python. Il permet de vérifier si un port est ouvert ou fermé, et affiche le nom du service associé s'il est disponible.

## Explication du code:
1) Options: Le programme supporte les scans TCP (-t), les scans UDP (-u), et une option d'aide (--help).
2) Plage de ports: Vous pouvez spécifier une plage de ports avec l'option -p (par exemple, 80 ou 80-85).
3) Services: Le programme affiche également le nom du service associé au port ouvert, en utilisant socket.getservbyport() pour récupérer les services standards (HTTP, FTP, etc.).
4) UDP ne garantit pas la réception d'une réponse comme TCP, c'est pourquoi le scanner ne peut pas toujours conclure que le port est ouvert s'il ne reçoit pas de réponse. En envoyant une réponse (ACK), vous permettez au scanner de vérifier que le port est bien ouvert.

**1. TCP (Transmission Control Protocol)**

Le TCP est un protocole de communication réseau orienté connexion. Imaginez-le comme une conversation téléphonique. Il établit une connexion fiable entre deux ordinateurs avant de commencer à échanger des données. Le TCP garantit que les données arrivent dans le bon ordre, sans corruption et de manière fiable. Voici ses principales caractéristiques :

- **Orienté connexion** : Une connexion est établie avant l'échange de données.
- **Fiabilité** : Les paquets de données sont envoyés et reçus dans l'ordre correct et sans corruption.
- **Contrôle de flux** : Le récepteur peut demander à l'émetteur de ralentir l'envoi de données s'il ne peut pas les traiter assez rapidement.

**2. UDP (User Datagram Protocol)**

L'UDP est un protocole de communication réseau sans connexion. Pensez-y comme à une carte postale. Les paquets de données (datagrammes) sont envoyés de manière indépendante, sans garantie d'arrivée ou d'ordre. L'UDP est plus rapide et plus léger que le TCP, mais il n'offre pas la même fiabilité.

**3. Socket (avec ses fonctions utilisées dans ce code)**

Un socket est une interface de programmation qui permet aux applications de communiquer sur un réseau. C'est un point de terminaison d'une connexion réseau. Votre code utilise le module `socket` de Python pour créer des sockets et effectuer des opérations réseau.

**4. Fonctions de socket utilisées dans le code:**

- `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` : Crée un socket TCP.
- `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)` : Crée un socket UDP.
- `sock.settimeout(1)` : Définit un délai d'attente d'une seconde pour les opérations de connexion et de réception.
- `sock.connect_ex((host, port))` : Tente d'établir une connexion TCP avec l'hôte et le port spécifiés. Renvoie 0 si la connexion est réussie.
- `sock.sendto(b"", (host, port))` : Envoie un datagramme vide (UDP) à l'hôte et au port spécifiés.
- `sock.recvfrom(1024)` : Reçoit un datagramme UDP de l'hôte distant, avec une taille maximale de 1024 octets.
- `sock.close()` : Ferme le socket.

**5. sys**

Le module `sys` fournit des fonctions et des variables liées à l'environnement d'exécution Python. Dans votre code, `sys` est utilisé pour :

- `sys.argv` : Accéder aux arguments de la ligne de commande passés au script.
- `sys.exit(1)` : Quitter le script avec un code de sortie différent de zéro, indiquant une erreur.

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