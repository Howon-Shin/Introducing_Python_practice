import zmq
from datetime import datetime

host = '127.0.0.1'
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)

server.bind(f'tcp://{host}:{port}')

request_bytes = server.recv()

if request_bytes == b'time':
    now_time = datetime.now().isoformat()

    reply_bytes = bytes(now_time, encoding= 'utf-8')
    server.send(reply_bytes)