from inspect import ClassFoundException
import pickle
import socket
import threading
import time
host = socket.gethostbyname(socket.gethostname())
port = 5566
ADDR = (host, port)
SIZE = 1024

def body_mass_index(weight, height):
    bmi = weight / pow(height, 2)

    return bmi

def daily_water(weight):
    daily_water = weight * 0.035

    return daily_water

def hearth_disease(abdominal_circ, sex):
    match sex:
        case 'M':
            if abdominal_circ <= 90:
                return 'Risk is normal'
            elif abdominal_circ > 90 and abdominal_circ < 94:
                return 'Risk is medium'
            elif abdominal_circ >= 94 and abdominal_circ < 102:
                return 'Risk is high'
            else:
                return 'Risk is very high'
        case 'F':
            if abdominal_circ <= 80:
                return 'Risk is normal'
            elif abdominal_circ > 80 and abdominal_circ < 84:
                return 'Risk is medium'
            elif abdominal_circ >= 84 and abdominal_circ < 88:
                return 'Risk is high'
            else:
                return 'Risk is very high'



def handle_client(clientsocket, addr):
    print("Got a connection from %s" % str(addr))

    measures = clientsocket.recv(SIZE)
    measures = pickle.loads(measures)

    weight = (measures[0])
    height = (measures[1])
    abdominal_circ = (measures[2])
    sex = measures[3]

    bmi = body_mass_index(weight, height)
    day_water = daily_water(weight)
    risk_disease = hearth_disease(abdominal_circ, sex)


    classifications = []
    classifications.append(bmi)
    classifications.append(day_water)
    classifications.append(risk_disease)
    
    classifications = pickle.dumps(classifications)
    time.sleep(45)
    clientsocket.send(classifications)

    clientsocket.close()



ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(ADDR)
ss.listen()
print("Server active on port %s.\n\r" % port)
while True:
    clientsocket, addr = ss.accept()
    t = threading.Thread(target=handle_client, args=(clientsocket, addr))
    t.start()
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    
    