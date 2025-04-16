import socket

HOST = '127.0.0.1'
PORT = 55555

send = input("Введите коэффициенты квадратного уравнения через пробел (a b c):\n")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(send.encode())
    data = s.recv(256)
    print('Результат:', data.decode())

