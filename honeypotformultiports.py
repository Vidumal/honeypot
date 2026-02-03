import socket
import logging
import threading


LISTENERS = [
    ('0.0.0.0', 8080, 'HTTP_Alt'),
    ('0.0.0.0', 2222, 'SSH_Alt'),
    ('0.0.0.0', 21,   'FTP'),     
    ('127.0.0.1', 9999, 'Internal_Test')
]

logging.basicConfig(filename='multi_honey.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def handle_connection(client_socket, addr, service):
    """Handles the interaction with the attacker"""
    try:
        print(f"[!] {service} connection from {addr[0]}")
        logging.info(f"Service: {service} | IP: {addr[0]}")

       
        if service == 'HTTP_Alt':
             response = "HTTP/1.1 200 OK\r\nServer: Apache\r\n\r\n<html><body><h1>It Works!</h1></body></html>"
             client_socket.sendall(response.encode())
        elif service == 'FTP':
             client_socket.send(b"220 ProFTPD 1.3.5 Server (Ubuntu)\r\n")
        else:
             client_socket.send(b"Welcome. Authorized access only.\r\n")

        
        data = client_socket.recv(1024)
        if data:
            print(f"    Payload ({service}): {data.decode('utf-8', errors='ignore').strip()}")
            logging.info(f"Payload ({service}): {data.decode('utf-8', errors='ignore').strip()}")
        
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

def start_listener(ip, port, service):
    """Starts a socket listener for a specific port"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        s.bind((ip, port))
        s.listen(5)
        print(f"[*] {service} Honeypot listening on {ip}:{port}...")
        
        while True:
            client, addr = s.accept()
            handle_connection(client, addr, service)
            
    except PermissionError:
        print(f"Failed to bind {ip}:{port} (Permission Denied). Did you use sudo?")
    except Exception as e:
        print(f"Error on {ip}:{port} -> {e}")


if __name__ == "__main__":
    print("Starting Honeypot")
    
    threads = []
    
    for ip, port, service in LISTENERS:
       
        t = threading.Thread(target=start_listener, args=(ip, port, service))
        t.daemon = True 
        t.start()
        threads.append(t)

   
    try:
        while True: 
            pass 
    except KeyboardInterrupt:
        print("\nStopping honeypot")