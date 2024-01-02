import socket
import threading
import argparse
import socks
import stem.process



# Start tor service
def start_tor():
    tor_service = stem.process.launch_tor_with_config(
        config={
            'SocksPort' : str(9050), # SOCKS default port 
            'ControlPort' : str(9051), # Control port to Tor Controller
        },
        timeout=300,
        take_ownership=True,
    )

    return tor_service
    

# Simple port Scanner
def scan_port(target, port, open_ports, lock):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((target, port))
            
            with lock:
                open_ports.append(port)
                print(f"[+] {port} Open!")

    except (socket.timeout, ConnectionRefusedError):
        pass  # Close Ports


# Threads to be fast
def scan_ports(target, init_port, end_port):
    open_ports = []
    lock = threading.Lock()
    threads = []

    for port in range(init_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port, open_ports, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return open_ports


def scan_ports_with_tor(target, init_port, end_port, tor_service):
    open_ports = []
    with socks.socksocket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        s.set_proxy(socks.SOCKS5, '127.0.0.1', 9050)
        s.connect((target, 80))


    for port in range(init_port, end_port + 1):
        try:
            s.connect((target, port))
            open_ports.append(port)
            print(f"[+] {port} Open!")

        except (socket.timeout, ConnectionRefusedError):
            pass # Close Port


    return open_ports

def main():

    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument('-t', '--target', required=True, help='Target')
    parser.add_argument('-a', '--all', action='store_true', help='For all ports')
    parser.add_argument('--tor', action='store_true', help='Use tor with port scanner')
    args = parser.parse_args()
    target = args.target
    all_ports = args.all
    tor_scanner = args.tor
    if all_ports:
        init_port = 1
        end_port = 65535
    else:
        init_port = 1
        end_port = 1024

    if tor_scanner:
        try:
            tor_service = start_tor()
            ports = scan_ports_with_tor(target, init_port, end_port, tor_service)
        except Exception as e:
            print(e)
    else:
        ports = scan_ports(target, init_port, end_port)

if __name__ == '__main__':
    main()