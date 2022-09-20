import math
import pickle
import socket

#****** A PRIMEIRA COISA A SE FAZER É DEFINIR O SOCKET, A PORTA E O ENDEREÇO *****
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 9999

#***** O MÉTODO BIND CONECTA O SOCKET A DEVIDA PORTA E ENDEREÇO *****
serverSocket.bind((host, port))

serverSocket.listen()
print('Server running...\n')

while True:
    clientSocket, addr = serverSocket.accept()
    print('Conectado a %s' % str(addr))

    data = clientSocket.recv(1024)
    data = pickle.loads(data)
    peso = data[0]
    altura = data[1]
    imc = peso / (altura * altura)

    imc = pickle.dumps(imc)

    clientSocket.send(imc)
    clientSocket.close()