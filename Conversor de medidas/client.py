# client.py
import socket
import pickle

repetirConversao = 's'
numConvertido = None

def escolhaGrandeza():
    print('\nBEM VINDO AO CONVERSOR DE MEDIDAS UNIVERSAL\n')
    print('ESCOLHA A GRANDEZA QUE DESEJA CdONVERTER:')

    print('1) Temperatura')
    print('2) Comprimento')
    print('3) Velocidade')
    print('4) Consumo de combustível\n')

    grandeza = int(input('Opção: '))
    while grandeza < 1 or grandeza >4:
        grandeza = int(input('ESCOLHA UMA GRANDEZA VÁLIDA: '))
            
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
    while conversao <1 or conversao >3:
        conversao = int(input('INFORME UMA OPÇÃO VÁLIDA: '))

    valor = int(input('\nINFORME O VALOR A SER CONVERTIDO: '))

    data.append(grandeza)
    data.append(conversao)
    data.append(valor)

    return data


while repetirConversao == 's':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 9999
    s.connect((host, port))
    data = []

    data = escolhaConversao()
    data = pickle.dumps(data)
    s.send(data)

    numConvertido = s.recv(1024)
    numConvertido = pickle.loads(numConvertido)
    print(numConvertido)

    repetirConversao = input('\nGostaria de fazer outra conversão? (s/n): ')
    s.close()

