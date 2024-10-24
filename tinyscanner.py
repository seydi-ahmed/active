import socket
import sys

# Affiche l'aide de commande
def print_help():
    help_text = """
Usage: tinyscanner [OPTIONS] [HOST] [PORT]
Options:
  -p               Range of ports to scan (e.g., 80, 80-85)
  -u               UDP scan
  -t               TCP scan
  --help           Show this message and exit.
"""
    print(help_text)

# Scanner de port TCP
def tcp_scan(host, port_range):
    start_port, end_port = parse_port_range(port_range)
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                service_name = socket.getservbyport(port, 'tcp')
                print(f"Port {port} is open (Service: {service_name})")
            else:
                print(f"Port {port} is closed")
            sock.close()
        except socket.error:
            print(f"Error scanning port {port}")
            continue

# Scanner de port UDP
def udp_scan(host, port_range):
    start_port, end_port = parse_port_range(port_range)
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                service_name = socket.getservbyport(port, 'udp')
                print(f"Port {port} is open (Service: {service_name})")
            else:
                print(f"Port {port} is closed")
            sock.close()
        except socket.error:
            print(f"Error scanning port {port}")
            continue

# Parser la plage de ports
def parse_port_range(port_range):
    if '-' in port_range:
        start_port, end_port = map(int, port_range.split('-'))
    else:
        start_port = end_port = int(port_range)
    return start_port, end_port

# Fonction principale
def main():
    if len(sys.argv) < 4 or '--help' in sys.argv:
        print_help()
        sys.exit(1)

    option = sys.argv[1]
    host = sys.argv[2]
    port_range = sys.argv[3].split('=')[-1]

    if option == '-t':
        print(f"Starting TCP scan on {host}...")
        tcp_scan(host, port_range)
    elif option == '-u':
        print(f"Starting UDP scan on {host}...")
        udp_scan(host, port_range)
    else:
        print("Invalid option. Use --help for more details.")
        sys.exit(1)

if __name__ == "__main__":
    main()
