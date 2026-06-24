import socket
import os
import time
from concurrent.futures import ThreadPoolExecutor

# VOID-SCAN Banner
print(r"""
 __      __   _     _  _____        _____  _____          _   _ 
 \ \    / /  (_)   | ||  __ \      / ____|/ ____|   /\   | \ | |
  \ \  / /__  _  __| || |  | |    | (___ | |       /  \  |  \| |
   \ \/ / _ \| |/ _` || |  | |     \___ \| |      / /\ \ | . ` |
    \  / (_) | | (_| || |__| |     ____) | |____ / ____ \| |\  |
     \/ \___/|_|\__,_||_____/     |_____/ \_____/_/    \_\_| \_|
""")

target_ip = input("[?] Target IP/Domain: ")
ports = range(1, 65536)
save_file = f"{target_ip}_report.txt"

def scan(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5) # Aggressive timeout for speed
        if s.connect_ex((target_ip, port)) == 0:
            output = f"[+] Port {port} Open\n"
            print(output, end="")
            with open(save_file, "a") as f:
                f.write(output)

print(f"[*] Scanning {target_ip}...")
start = time.time()

# Using 500 threads for maximum throughput
with ThreadPoolExecutor(max_workers=500) as executor:
    executor.map(scan, ports)

duration = time.time() - start
print(f"[*] Scan finished in {duration:.2f} seconds.")
print(f"[*] Report: {save_file}")