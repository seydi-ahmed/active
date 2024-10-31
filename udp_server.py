import socket

UDP_IP = "0.0.0.0"  # Écoute sur toutes les interfaces réseau
UDP_PORT = 8080  # Numéro de port à occuper

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for UDP on port {UDP_PORT}")

# Boucle pour maintenir le port occupé
while True:
    data, addr = sock.recvfrom(1024)  # Taille de tampon 1024 octets
    print(f"Received message: {data} from {addr}")
    # Envoyer une réponse au client
    sock.sendto(b"ACK", addr)
