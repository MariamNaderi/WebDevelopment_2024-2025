import socket

def solve_quadratic(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        return "Нет действительных корней"
    elif D == 0:
        x = -b / (2*a)
        return f"Один корень: {x:.4f}"
    else:
        x1 = (-b - D**0.5) / (2*a)
        x2 = (-b + D**0.5) / (2*a)
        return f"Два корня: {x1:.4f}, {x2:.4f}"

HOST = '127.0.0.1'
PORT = 55555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Сервер запущен и ждет подключения...')
    conn, addr = s.accept()
    with conn:
        print(f"Подключен клиент: {addr}")
        data = conn.recv(256).decode()
        try:
            a, b, c = map(float, data.split())
            answer = solve_quadratic(a, b, c)
        except:
            answer = "Ошибка ввода данных"
        conn.sendall(answer.encode())
