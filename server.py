import socket
import threading
from time import sleep

HOST = 'localhost'  # 127.0.0.1
PORT = 5000

def handle_client(socket_client, client_address):
    print(f'Conectado em {client_address}')

    while True:
        data = socket_client.recv(4096)
        data = data.decode()
        if not data:
            print(f'Sem dados recebidos do client: {client_address}, encerrando conexão...')
            socket_client.close()
            break

        print(f'Mensagem recebida do cliente {client_address}: {data}')
        socket_client.sendall(data.encode())
        print(f"Mensagem '{data}' enviada ao client {client_address}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:  # criando um socket do tipo TCP
    socket_server.bind((HOST, PORT))  # associa um socket a um endereço e uma porta especifica
    socket_server.listen()
    print('Aguardando conexão de um cliente')

    while True:  # fica sempre procurando conexões
        socket_client, client_address = socket_server.accept()
        client_thread = threading.Thread(target=handle_client, args=(socket_client, client_address)) # cria uma thread para cada cliente conectado
        client_thread.start()
