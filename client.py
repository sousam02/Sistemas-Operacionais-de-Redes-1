# client.py
import socket
import pickle
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
s.connect((host, port))
data = []
print("\n### conversor de frases ###\n\n")
frase = input("Digite a frase a ser enviada:\n")
print("1. Converter para MAIÚSCULAS;\n")
print("2. Converter para minúsculas;\n")
opcao = int(input("Qual a opção desejada?\n"))
data.append(opcao)
data.append(frase)
s.send(pickle.dumps(data))
nova_frase = s.recv(1024)
nova_frase = pickle.loads(nova_frase)
s.close()
print("\nA nova frase é: %s\n" % nova_frase)