from datetime import datetime
import socket

server_addr = ('localhost', 6789)
max_size = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_addr)

data, client = server.recvfrom(max_size)

if data == b'time':
    now_time = datetime.now().isoformat()

    server.sendto(bytes(now_time, encoding= 'utf-8'), client)

server.close()