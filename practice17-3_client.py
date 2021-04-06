import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:6789/')

now_time = proxy.now_time('time')

print(now_time)