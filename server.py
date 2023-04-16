import socket

HOST = 'localhost' # 127.0.0.1
PORT = 50000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server: # criando um socket do tipo TCP

    socket_server.bind((HOST, PORT)) # associa um socket a um endereço e uma porta especifica
    socket_server.listen()
    print('Aguardando conexão de um cliente')
    socket_client, client_address = socket_server.accept()
    print('Conectado em', client_address)


    while True:
        data = socket_client.recv(4096)
        if not data: # se recebeu alguma mensagem == V
                print('Fechando a conexão')
                socket_client.close()
                break
        socket_client.sendall(data)

# O socket será fechado automaticamente ao sair do bloco with
