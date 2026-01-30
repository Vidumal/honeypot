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

while True:
       
        client_socket, addr = s.accept()
        print(f"[!] Alert: Connection from {addr[0]}:{addr[1]}")
        logging.info(f"Connection from: {addr[0]}")

        try:
        
            client_socket.send(b"Welcome to Ubuntu 20.04 LTS. Login: ")
            
            
            data = client_socket.recv(1024)
            print(f"[+] Attacker tried: {data.decode('utf-8').strip()}")
            logging.info(f"Payload: {data.decode('utf-8').strip()}")
            
        
            client_socket.close()
        except Exception as e:
            client_socket.close()
