from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime

def now_time(text):
    if text == 'time':
        now = datetime.now().isoformat()

        return now

server = SimpleXMLRPCServer(('localhost', 6789))
server.register_function(now_time, 'now_time')
server.serve_forever()