#Imports
import socket
import json
import time

def pingOVS(HOST, PORT):
	#String to send in raw JSON over TCP
	#This particular string is the properly formatted OVSDB echo function. 
	#The server (OVS) should return the exact same string back to us.
	jsonString = "{\"method\": \"echo\",\"id\": \"echo\",\"params\": []}"

	#Create socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#Establish TCP session via IP address and port specified
	s.connect((HOST, PORT))

	#Send JSON to socket
	print "Sending echo request =====>"
	s.send(json.dumps({'method':'echo','id':'echo','params':[]}))

	#Wait for response and print to console
	result = json.loads(s.recv(1024))
	print "<========" + str(result)
	time.sleep(2)

while True:
	pingOVS("10.12.0.30", 6634)

#Exit
s.close()
