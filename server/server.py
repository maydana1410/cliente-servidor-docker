import socket
import threading

HOST = '0.0.0.0'
PORT = 5100

ingressos_disponiveis = 100
lock = threading.Lock()

def handle_client(conn, addr):
    global ingressos_disponiveis

    with lock:
        if ingressos_disponiveis > 0:
            ingressos_disponiveis -= 1
            resposta = "Reserva Confirmada\n"
        else:
            resposta = "Ingressos Esgotados\n"

    conn.sendall(resposta.encode())
    conn.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(100)

    print(f"[SERVIDOR] Rodando em {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start_server()
