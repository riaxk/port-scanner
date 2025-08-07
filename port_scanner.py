import socket
from datetime import datetime

# Target input
target = input("Enter the IP address to scan: ")
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
start_time = datetime.now()

try:
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()
except KeyboardInterrupt:
    print("\nScan stopped by user.")
except socket.error:
    print("Could not connect to server.")
    
end_time = datetime.now()
print(f"\nScanning completed in: {end_time - start_time}")

