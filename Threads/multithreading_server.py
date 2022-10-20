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

    data = ['Body mass index']
    if bmi >= 18.5 and bmi < 25:
        return data + ['BMI >= 18.5 and < 25','Normal']
    elif bmi >= 25 and bmi < 30:
        return data + ['BMI >= 25 and < 30','Overweight']
    elif bmi >= 30 and bmi < 40:
        return data + ['BMI >= 30 and < 40','Obesity']
    elif bmi >= 40:
        return data + ['BMI >= 40','Severe obesity']

    return bmi

def daily_water(weight):

    daily_water = weight * 0.035

    return ['Daily water','Weight * 0.035','{:.2f} Liters'.format(daily_water)]

def hearth_disease(abdominal_circ, sex):
    match sex:
        case 'M':
            risk_disease = ['Hearth disease risk']
            if abdominal_circ <= 90:
                return risk_disease + ['Abdominal circumference <= 90 cm','Risk is normal']
            elif abdominal_circ > 90 and abdominal_circ < 94:
                return risk_disease + ['Abdominal circumference > 90 cm','Risk is medium']
            elif abdominal_circ >= 94 and abdominal_circ < 102:
                return risk_disease + ['Abdominal circumference >= 94 cm','Risk is high']
            elif abdominal_circ >= 102:
                return risk_disease + ['Abdominal circumference >= 102 cm','Risk is very high']
        case 'F':
            if abdominal_circ <= 80:
                return risk_disease + ['Abdominal circumference <= 80 cm','Risk is normal']
            elif abdominal_circ > 80 and abdominal_circ < 84:
                return risk_disease + ['Abdominal circumference > 80 cm','Risk is medium']
            elif abdominal_circ >= 84 and abdominal_circ < 88:
                return risk_disease + ['Abdominal circumference >= 84 cm','Risk is high']
            elif abdominal_circ >= 88:
                return risk_disease + ['Abdominal circumference >= 88 cm','Risk is very high']



def handle_client(clientsocket, addr):
    print("Got a connection from %s" % str(addr))

    measures = clientsocket.recv(SIZE)
    measures = pickle.loads(measures)

    weight = measures[0]
    height = measures[1]
    abdominal_circ = measures[2]
    sex = measures[3]

    bmi = body_mass_index(weight, height)
    day_water = daily_water(weight)
    risk_disease = hearth_disease(abdominal_circ, sex)
    
    classifications = [
        {
            'information': bmi[0],
            'calculation': bmi[1],
            'classification': bmi[2]
        },
        {
            'information': day_water[0],
            'calculation': day_water[1],
            'classification': day_water[2]
        },
        {
            'information' : risk_disease[0],
            'calculation': risk_disease[1],
            'classification': risk_disease[2]
        }
    ]
        
    
    
    classifications = pickle.dumps(classifications)
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
    
    