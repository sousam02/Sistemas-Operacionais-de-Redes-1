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
                    conversao = 'Celsius: {} - Fahrenheit: {}'.format(data[2], numConvertido)
                    
                case 2:
                    numConvertido = (valor - 32) * 5/9
                    conversao = 'Fahrenheit: {} - Celsius: {}'.format(data[2], numConvertido)

                case 3:
                    numConvertido = valor + 273,15
                    conversao = 'Celsius: {} - Kelvin: {}'.format(data[2], numConvertido)
        case 2:
            match conversao:
                case 1:
                    numConvertido = valor * 100
                    conversao = 'Metro: {} - Centimetro: {}'.format(data[2], numConvertido)
                case 2:
                    numConvertido = valor / 100
                    conversao = 'Centimetro: {} - Metro: {}'.format(data[2], numConvertido)
                case 3:
                    numConvertido = valor / 1000
                    conversao = 'Metro: {} - Quilometro: {}'.format(data[2], numConvertido)
        case 3:
            match conversao:
                case 1:
                    numConvertido = valor * 3.6
                    conversao = 'Metro por segundo: {} - Quilômetro por hora: {}'.format(data[2], numConvertido)
                case 2:
                    numConvertido = valor / 1.609
                    conversao = 'Quilometro por hora: {} - Milha por hora: {}'.format(data[2], numConvertido)
                case 3:
                    numConvertido = valor * 1.688
                    conversao = 'Nó: {} - Pés por segundo: {}'.format(data[2], numConvertido)
        case 4:
            match conversao:
                case 1:
                    numConvertido = valor * 2.35215
                    conversao = 'Quilômetro por litro: {} - Milha por galão americano: {}'.format(data[2], numConvertido)
                case 2:
                    numConvertido = valor * 1.201
                    conversao = 'Milha por galão americano: {} - Milha por galão imperial: {}'.format(data[2], numConvertido)
                case 3:
                    numConvertido = valor / 2.825
                    conversao = 'Milha por galão imperial: {} - Quilômetro por litro: {}'.format(data[2], numConvertido)
    conversao = pickle.dumps(conversao)

    clientsocket.send(conversao)
    clientsocket.close()