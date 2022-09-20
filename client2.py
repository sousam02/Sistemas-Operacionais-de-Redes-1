import socket
import pickle

# ***** PARA O CLIENTE, O PROCESSO INICIAL É O MESMO *****

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 9999

clientSocket.connect((host, port))
data = []

peso = int(input('Informe seu peso\n'))
altura = float(input('informe sua altura\n'))

data.append(peso)
data.append(altura)
print(data[0])
print(data[1])

clientSocket.send(pickle.dumps(data))

imc = clientSocket.recv(1024)
imc = pickle.loads(imc)
clientSocket.close()

print('Seu Índice de Massa Corporal é: %f' % imc)
