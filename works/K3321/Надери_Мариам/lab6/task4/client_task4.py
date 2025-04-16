import socket
import threading

# получение сообщений от сервера
def messages_get(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                print("\nСоединение с сервером разорвано")
                client.close()
                break
            print(message)
        except (ConnectionResetError, OSError):
            print("\nСоединение с сервером разорвано")
            client.close()
            break


# отправка сообщений на сервер
def messages_send(client):
    try:
        while True:
            message = input()
            if message.lower() == 'exit':
                client.close()
                break
            client.send(message.encode('utf-8'))
    except (ConnectionResetError, OSError):
        pass


HOST = '127.0.0.1'
PORT = 55555
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
            
        # получаем запрос никнейма
        nickname = input(s.recv(1024).decode('utf-8') + " ")
        s.send(nickname.encode('utf-8'))
            
        # получаем приветственное сообщение
        print(s.recv(1024).decode('utf-8'))
            
        # поток для получения сообщений
        thread_get = threading.Thread(target=messages_get, args=(s,))
        #thread_get.daemon = True
        thread_get.start()
            
        # поток для отправки сообщений (в основном потоке)
        messages_send(s)
            
    except ConnectionRefusedError:
        print("Не удалось подключиться к серверу")
    except KeyboardInterrupt:
        print("\nВыход из программы")

