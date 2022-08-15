import socket
import server


sock = socket.socket()
sock.connect((server.host,server.port))
print(sock.recv(1024))
sock.close()

#creating a client with UDP protocol
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg = 'Hi, there so glad to be connected to you.'
s.sendto(msg,(server.new_host, server.new_port))