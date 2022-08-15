import socket
soc = socket.socket()
host = socket.gethostname()
port = 12345
soc.bind((host, port))
print('server is waiting for connection...')
soc.listen(5)
conn, address = soc.accept()
while True:
    data = conn.recv(1024)
    if not data: break
    soc.sendall(data)
soc.close()

#server manipulates data before sending to client
s = socket.socket()
s.bind((host, port))
s.list(5)
conn, addr = s.accept()
print('Connection successful.')
while True:
    data = s.recv(1024)
    dat = data.split(',')
    result = int(dat[0]) + int(dat[1])
    s.sendall(str(result))
s.close()