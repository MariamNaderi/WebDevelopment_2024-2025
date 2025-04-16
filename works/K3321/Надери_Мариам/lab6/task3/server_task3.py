import socket

# Загрузка html-страницы
try:
    with open("index.html", "r", encoding='utf-8') as file:
        content = file.read()
        status = "HTTP/1.1 200 OK"
except:
    content = '<html><body><h1>Error: index.html not found</h1></body></html>'
    status = "HTTP/1.1 404 Not Found"

# http-ответ
response = f"""{status}
Content-Type: text/html; charset=utf-8
Content-Length: {len(content.encode('utf-8'))}

{content}"""

HOST = '127.0.0.1'  
PORT = 55555        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))     
    s.listen()             
    print(f"Сервер запущен. Откройте в браузере: http://{HOST}:{PORT}")


    conn, addr = s.accept()  
    with conn:
        print("Подключился:", addr)  
        print('\nПолученный запрос:\n', conn.recv(256).decode('utf-8'))
        conn.sendall(response.encode('utf-8')) 
        print("\nHTML-страница отправлена")
    s.close()