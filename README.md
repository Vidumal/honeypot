# Multi-Service Python Honeypot 🍯

A lightweight, multi-threaded honeypot written in Python designed to simulate various network services (HTTP, SSH, FTP) simultaneously. This tool listens for incoming connections, logs the attacker's IP address, and captures the initial payload or command sent.

**Current Status:** v1.0 (Educational/Prototype)

## 📋 Features
* **Multi-Threaded Architecture:** Listens on multiple ports and IP addresses at the same time without blocking.
* **Service Simulation:** Mimics basic service banners (e.g., sending an Apache server header for HTTP or a ProFTPD banner for FTP).
* **Live Logging:** Records timestamp, attacker IP, target service, and payload to both the console and a local log file (`multi_honey.log`).
* **Configurable:** Easy to add or remove listeners via the Python configuration list.
* **Standard Library Only:** No external `pip` dependencies required.

## ⚠️ Legal & Security Disclaimer
**FOR EDUCATIONAL PURPOSES ONLY.**
This software is intended for learning about network security, honeypots, and monitoring.
* **Do not** deploy this on a production server containing sensitive data.
* **Do not** use this tool to engage in "hacking back" or aggressive countermeasures.
* **Do not** run this on a network where you do not have permission to monitor traffic.
* The author is not responsible for any damage caused by the use of this tool.

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Vidumal/honeypot.git](https://github.com/Vidumal/honeypot.git)
    cd multi-service-honeypot
    ```

2.  **Ensure Python 3 is installed:**
    ```bash
    python3 --version
    ```

## ⚙️ Configuration
Open `multi_honey.py` in your text editor. Locate the `LISTENERS` list at the top of the file to configure which ports and IPs to monitor.

```python
# Format: ('IP_Address', Port, 'Service_Name')
LISTENERS = [
    ('0.0.0.0', 8080, 'HTTP_Alt'),      # Listens on all interfaces
    ('0.0.0.0', 2222, 'SSH_Alt'),
    ('127.0.0.1', 9999, 'Internal_Test') # Localhost only
]