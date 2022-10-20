import socket
import pickle
host = socket.gethostbyname(socket.gethostname())
port = 5566
ADDR = (host, port)
SIZE = 1024
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'


def menu():    
    print('====HEALTH MEASURES===='.center(60))
    print('THE PROCESS IS SIMPLE, YOU ONLY NEED TO ENTER THREE MEASURES AND YOUR SEX:\n')
    print('1- WEIGHT (KG)\n2- HEIGHT (CM)\n3- ABDOMINAL CIRCUNFERENCE (CM)\n4- SEX (M or W)\n')

    weight = float(input('INFORM YOUR WEIGHT (KG): '))
    height = float(input('INFORM YOUR HEIGHT (CM): ')) / 100
    abdominal_circ = float(input('INFORM YOUR ABDOMINAL CIRCUMFERENCE (CM): '))
    
    sex = input('INFORM YOUR SEX (M or F): ').capitalize()
    while sex != 'M' and sex != 'F':
        sex = input('INFORM A VALID SEX (M or F): ').capitalize()
    

    measures = []
    measures.append(weight)
    measures.append(height)
    measures.append(abdominal_circ)
    measures.append(sex)

    return measures

measures = menu()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f'\n[CONNECTED] client connected at {host}:{port}')

client.send(pickle.dumps(measures))

classifications = client.recv(SIZE)
classifications = pickle.loads(classifications)

print('+------------------------------------------+-------------------------------------+------------------------------+')
print("|{:^42}|{:^37}|{:^30}|".format('INFORMATION', 'CALCULATION', 'CLASSIFICATION'))

for i in range(len(classifications)):
    print('+------------------------------------------+-------------------------------------+------------------------------+')
    print("|{information:<42}|{calculation:37}|{classification:30}|".format(**classifications[i]))
print('+------------------------------------------+-------------------------------------+------------------------------+')


client.close()


   