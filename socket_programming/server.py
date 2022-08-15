import socket

# working with TCP protocol
# creating a server side socket
soc = socket.socket()
host = socket.gethostname()
port = 9999
soc.bind((host, port))
print('waiting for connection...')
soc.listen(5)
while True:
    conn, address = soc.accept()
    print('Connected to',address)
    conn.send('server confirmed connection')
    soc.close()

#creating a server with UDP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
new_host = socket.gethostname()
new_port = 12345
print('Waiting for connection...')
s.list(3)
while True:
    data, address = s.recvfrom(1024)
    print('Received messages {data} from {address}'.format(data, address))





