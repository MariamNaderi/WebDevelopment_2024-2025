import socket
import threading

clients = {}  # ключ - сокет, значение - никнейм

# отправка сообщения всем клиентам кроме отправителя
def send_everybody(message, sender=None):
    disconnected_clients = []
    for client in clients.keys():
        if client != sender:
            try:
                client.send(message.encode('utf-8'))
            except:
                disconnected_clients.append(client)

    for client in disconnected_clients:
        if client in clients:
            nickname = clients.pop(client)
            send_everybody(f'{nickname} покинул чат!')

# обработка сообщений от клиента
def chat_for_client(client):
    try:
        client.send('Введите свой никнейм: '.encode('utf-8'))
        clients[client] = client.recv(1024).decode('utf-8')
            
        print(f'Подключился: {clients[client]}')
        send_everybody(f'{clients[client]} присоединился к чату!')
        client.send(f'Добро пожаловать, {clients[client]}!'.encode('utf-8'))
        
        while True:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
            send_everybody(f'{clients[client]}: {message}')
            
    except (ConnectionResetError, ValueError) as e:
        print(f"{clients[client]} отключился")
    finally:
        if client in clients:
            nickname = clients.pop(client)
            send_everybody(f'{nickname} покинул чат!')
        client.close()


HOST = '127.0.0.1'
PORT = 55555
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print('Сервер запущен и ждет подключения...')
        
    while True:
        conn, addr = s.accept()
        print(f"Подключен клиент: {addr}")
            
        # Запуск потока для клиента
        thread = threading.Thread(target=chat_for_client, args=(conn,))
        thread.start()

