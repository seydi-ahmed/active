import socket
import sys

port_service_mapping = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP Proxy",
}

def get_service_name(port):
    return port_service_mapping.get(port, "Unknown Service")

def tcp_scan(host, port_range):
    start_port, end_port = parse_port_range(port_range)
    # print(f"Starting TCP scan on {host}...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout pour les connexions
        result = sock.connect_ex((host, port))
        if result == 0:
            service_name = get_service_name(port)  # Récupérer le nom du service
            print(f"Port {port} is open ({service_name})")
        else:
            print(f"Port {port} is closed")
        sock.close()

def udp_scan(host, port_range):
    start_port, end_port = parse_port_range(port_range)
    # print(f"Starting UDP scan on {host}...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        try:
            sock.sendto(b"", (host, port))
            data, addr = sock.recvfrom(1024)
            service_name = get_service_name(port)  # Récupérer le nom du service
            print(f"Port {port} is open ({service_name})")
        except socket.timeout:
            print(f"Port {port} is closed")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
        finally:
            sock.close()

def parse_port_range(port_range):
    try:
        if '-' in port_range:
            start_port, end_port = map(int, port_range.split('-'))
        else:
            start_port = end_port = int(port_range)
        return start_port, end_port
    except ValueError:
        print("Invalid port number. Please specify a valid integer.")
        sys.exit(1)

def main():
    if len(sys.argv) < 5:
        print("Usage: python3 tinyscanner.py [OPTIONS] [HOST] -p [PORT]\nOptions:\n  -p               Range of ports to scan\n  -u               UDP scan\n  -t               TCP scan\n  --help           Show this message and exit.")
        sys.exit(1)

    command = sys.argv[1]
    host = sys.argv[2]
    port_arg = sys.argv[3]
    port_range = sys.argv[4]

    if port_arg != "-p":
        print("Invalid usage. Please use -p to specify the port.")
        sys.exit(1)

    if command == "-t":
        tcp_scan(host, port_range)
    elif command == "-u":
        udp_scan(host, port_range)
    else:
        print("Invalid command. Use -t for TCP scan or -u for UDP scan.")
        sys.exit(1)

if __name__ == "__main__":
    main()
