# client.py
import socket
import pickle
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
s.connect((host, port))
repetirConversao = 's'
while repetirConversao == 's':
    data = []

    def escolhaGrandeza():
        print('\nBEM VINDO AO CONVERSOR DE MEDDAS UNIVERSAL\n')
        print('ESCOLHA A GRANDEZA QUE DESEJA CONVERTER:')

        print('1) Temperatura')
        print('2) Comprimento')
        print('3) Velocidade')
        print('4) Consumo de combustível\n')

        grandeza = int(input('Opção: '))
        
        return grandeza

    def escolhaConversao():
        grandeza = escolhaGrandeza()

        print('\nESCOLHA O TIPO DE CONVERSÃO: ')

        match grandeza:
            case 1: 
                print('1) Celsius - Fahrenheit')
                print('2) Fahrenheit - Celsius')
                print('3) Celsius - Kelvin\n')

            case 2:
                print('1) Metro - Centímetro')
                print('2) Centímetro - Metro')
                print('3) Metro - Quilômetro\n')

            case 3:
                print('1) Metro por segundo - Quilômetro por hora')
                print('2) Quilômetro por hora - Milha por hora')
                print('3) Nó - Pés por segundo\n')

            case 4:
                print('1) Quilômetro por litro - Milha por galão americano')
                print('2) Milha por galão americano - Milhas por galão imperial')
                print('3) Milhas por galão imperial - Quilômetro por litro\n')
                
        conversao = int(input('Opção: '))

        valor = int(input('\nINFORME O VALOR A SER CONVERTIDO: '))

        data.append(grandeza)
        data.append(conversao)
        data.append(valor)

        return data

    data = escolhaConversao()
    data = pickle.dumps(data)

    s.send(data)

    numConvertido = s.recv(1024)
    numConvertido = pickle.loads(numConvertido)
    print('O valor convertido é: %5.2f' % numConvertido)

    repetirConversao = input('\nGostaria de fazer outra conversão? (s/n)')
s.close()

