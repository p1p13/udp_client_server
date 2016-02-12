from socket import *
serverName='localhost'
servePort=12000
clientSocket=socket(AF_INET,	SOCK_DGRAM)
sentence=raw_input('Input Lowercase sentence:')
clientSocket.sendto(sentence,(serverName,servePort))
newSentence,serverAddress=clientSocket.recvfrom(2048)
print newSentence
clientSocket.close()