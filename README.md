# VOID-SCAN
**High-Performance Multi-Threaded Port Scanner**

VOID-SCAN is a custom-built, multi-threaded network reconnaissance tool designed for speed and efficiency. It allows security enthusiasts and penetration testers to identify open services across the entire 1-65535 port range rapidly.

## Features
- **High Concurrency:** Utilizes `ThreadPoolExecutor` for high-speed scanning.
- **Dynamic Reporting:** Automatically generates unique reports based on the target.
- **Service Enumeration:** Attempts to grab service banners from open ports.
- **Stealth-Adjustable:** Built-in timeout controls for efficient network utilization.

## Usage
1. Clone the repository: `git clone https://github.com/yourusername/VOID-SCAN`
2. Run the script: `python void_scan.py`
3. Enter the target IP or domain when prompted.

## Disclaimer
*This tool is for educational purposes and authorized security testing only. The author assumes no liability for misuse.*
