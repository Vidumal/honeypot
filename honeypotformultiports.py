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
