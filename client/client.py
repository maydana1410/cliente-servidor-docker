import socket
import threading
import time

SERVER_HOST = 'server'
SERVER_PORT = 5100

def comprar():
    for _ in range(10):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((SERVER_HOST, SERVER_PORT))

            resposta = client.recv(1024).decode()
            print(resposta.strip())

            client.close()
            return
        except:
            time.sleep(0.2)

    print("Falha ao conectar")


def gerar_requisicoes():
    threads = []

    time.sleep(2)

    for _ in range(100):
        t = threading.Thread(target=comprar)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == "__main__":
    gerar_requisicoes()
