# server.py
import socket
import pickle
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = '127.0.0.1'
port = 9999
# bind to the port
serversocket.bind((host, port))
# starts listening requests
serversocket.listen()
print("Server running...\n")
while True:
    # establish a connection
    clientsocket, addr = serversocket.accept() # bloqueado
    print("Conectado a %s" % str(addr))
    data = clientsocket.recv(1024)
    data = pickle.loads(data)
    
    grandeza = data[0]
    conversao = data[1]
    valor = data[2]

    match grandeza:
        case 1:
            match conversao:
                case 1:
                    numConvertido = (valor * 9/5) + 32
                case 2:
                    numConvertido = (valor - 32) * 5/9
                case 3:
                    numConvertido = valor + 273,15
        case 2:
            match conversao:
                case 1:
                    numConvertido = valor * 100
                case 2:
                    numConvertido = valor / 100
                case 3:
                    numConvertido = valor / 1000
        case 3:
            match conversao:
                case 1:
                    numConvertido = valor * 3.6
                case 2:
                    numConvertido = valor / 1.609
                case 3:
                    numConvertido = valor * 1.688
        case 4:
            match conversao:
                case 1:
                    numConvertido = valor * 2.35215
                case 2:
                    numConvertido = valor * 1.201
                case 3:
                    numConvertido = valor / 2.825
    print(numConvertido)
    numConvertido = pickle.dumps(numConvertido)

    clientsocket.send(numConvertido)
    clientsocket.close()