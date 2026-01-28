import socket
import logging

logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def start_honeypot(ip='0.0.0.0', port=2222):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

    try:
        s.bind((ip, port))
        s.listen(5)
        print(f"[*] Honeypot listening on {ip}:{port}...")
    except Exception as e:
        print(f"Error: {e}")
        return

