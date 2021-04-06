import socket

server_addr = ('localhost', 6789)
max_size = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Sending time')
client.sendto(b'time', server_addr)

data, server = client.recvfrom(max_size)

print(data)

client.close()