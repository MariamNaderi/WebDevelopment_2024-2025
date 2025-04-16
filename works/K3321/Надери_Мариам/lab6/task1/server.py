import socket

HOST = '127.0.0.1'      # localhost/локальный адрес  
PORT = 55555            # любой свободный порт для прослушивания больше 1024  

# создаем сокет с настройками: AF_INET - использование IPv4, SOCK_STREAM - TCP соединение
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))                                            # привязываем сокет к адерсу и порту
    s.listen()                                                      # слушаем
    print('Сервер запущен и ждет подключения...')
    # принмает подключение, conn - нлвый сокет для общения, addr - ip + порт клиента
    conn, addr = s.accept()                                         

    with conn:
        print(f"Подключен клиент: {addr}")
        data = conn.recv(32)                                      # получаем данные (макс 32 байта)
        print(f"Получено сообщение от клиента: {data.decode()}")
        conn.sendall(b"Hello, client")                              # отправка сообщ, преобразуется в байты (b)

