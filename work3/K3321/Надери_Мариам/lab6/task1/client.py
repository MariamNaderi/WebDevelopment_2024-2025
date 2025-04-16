import socket

HOST = '127.0.0.1'      # localhost/локальный адрес  
PORT = 55555            # любой свободный порт для прослушивания больше 1024        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))                                  # подключение к серверу
    s.sendall(b"Hello, server")                              # отправка сообщ, преобразуется в байты (b)
    data = s.recv(32)                                        # получаем данные (макс 32 байта)
    print(f"Ответ от сервера: {data.decode()}")


