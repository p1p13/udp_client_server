from socket import *
serverPort=12000
serverSocket=socket(AF_INET	,SOCK_DGRAM)
serverSocket.bind(('localhost',serverPort))
print 'server ready'
while 1:
	sentence,cadr=serverSocket.recvfrom(2048)
	newSentence=sentence.upper()
	serverSocket.sendto(newSentence,cadr)
	