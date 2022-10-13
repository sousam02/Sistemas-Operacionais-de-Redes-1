from ast import arg
import threading
import time
ls = []

def count(n):
    for i in range(1, n+1):
        ls.append(i)
        print(ls)
        time.sleep(0.5)
        
def count2(n):
    for i in range(1, n+1):
        ls.append(i)
        print(ls)
        time.sleep(0.5)

#instanciamento e inicialização da primeira thread
x = threading.Thread(target=count, args=(5,))
x.start()

#instanciamento e inicialização da segunda thread
y = threading.Thread(target=count2, args=(5,))
y.start()


#o fluxo só seguirá quando as threads x e y finalizarem
x.join()
y.join()

print(ls)