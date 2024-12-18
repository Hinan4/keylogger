import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    """Scan a single port to check if it's open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            print(f"[+] Port {port} is open on {ip}")
    except:
        pass  # Port is closed or unreachable

def main():
    target_ip = input("Enter the target IP address: ")
    port_range = input("Enter port range (e.g., 1-1000): ")
    
    # Parse the port range
    start_port, end_port = map(int, port_range.split('-'))
    
    print(f"Scanning {target_ip} for open ports from {start_port} to {end_port}...\n")
    
    # Use a thread pool to speed up the scanning process
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target_ip, port)

if __name__ == "__main__":
    main()
