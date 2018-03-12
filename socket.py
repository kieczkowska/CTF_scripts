# reusable: the script creates a socket to connect to a given host
# so you can receive and send stuff.
# challenge: receive equations in string format and automate their
# evaluation + send the output back to get a flag including the string
# "enusec".

#this is the reusable part
import socket
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = raw_input("Host: ")
port = raw_input("Port number: ")
port = int(port)
s.connect( (host, port) )

# this is the challenge specific part
print("Received from host: ", s.recv(300))
from_host = ""
while "enusec" not in from_host:
	from_host =  s.recv(200)
	print("Received from host: " , from_host)

	arr = from_host.strip(" ").split(" ")
	equation = ""

	for x in arr:
		if "=" not in x:
			equation += x

	answer = str(eval(equation))
	s.send(answer)
