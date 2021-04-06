import zmq

host = '127.0.0.1'
port = 6789
context = zmq.Context()
sub = context.socket(zmq.SUB)
sub.connect(f'tcp://{host}:{port}')

sub.setsockopt(zmq.SUBSCRIBE, b'')

while True:
    word_bytes = sub.recv()

    word = word_bytes.decode('utf-8')
    
    if word.startswith(tuple('aeiouAEIOU')):
        print(word)