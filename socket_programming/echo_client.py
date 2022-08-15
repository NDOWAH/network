import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host,port))
s.sendall('This will be sent to the server.')
data = s.recv(1024)
print(data)
s.close()
#client sending data to server for manipulating and returning results
a = input("Enter first number: ")
b = input("Enter second number: ")
c = a+ ","+b
soc = socket.socket()
soc.connect((host, port))
print("Sending{0} to the server".format(c))
soc.sendall(c)
data = soc.recv(1024)
soc.close()
