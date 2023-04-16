import socket

'''
    Constantes e atributos de sockets

        socket.family: família do socket criado
        socket.type: tipo do socket criado
        socket.proto: protocolo associado ao socket

    Criar objeto socket

        Criamos um objeto do tipo socket usando o método socket.socket(), o qual recebe dois ou três parâmetros (um é opcional)

        Família de Endereços

            AF_INET (endereço IPv4)
            AF_INET6 (endereço IPv6)

        Tipo de Socket

            SOCK_STREAM (para socket TCP)
            SOCK_DGRAM (para socket UDP)

        Protocolo (variação do protocolo em uma família)

            Geralmente, zero.


    Métodos de um objeto socket

        accept(): aceita uma conexão de cliente.

        bind(endereço): associa o socket servidor a um endereço.

        close(): fecha um socket, liberando todos os recursos alocados.

        connect(endereço) conecta um cliente a um endereço.

        connect_ex(endereço) idem anterior, retornando um indicador de erro, em vez de uma exceção, na ocorrência da chamada do connect em baixo nível.

        getpeername() retorna o endereço do socket remoto com o qual um socket local está associado.

        getsockname(): retorna o endereço do socket local.

        listen(): é usado para colocar um socket em modo de escuta.

    Métodos paa envio e leitura de bytes

    recv(bufsize[, flags]): lê os bytes recebidos, retornando-os em uma string, até o limite de buffer definido por buffsize.

    recvfrom(bufsize[, flags]): (UDP) lê os bytes recebidos, retornando-os em uma string, até o limite de buffer definido por buffsize.

    send(bytes[, flags]): solicita o envio dos bytes pelo socket até que um certo conjunto de bytes seja enviado - buffer suficiente para garantir o envio.

    sendall(bytes[, flags]): envia todos os bytes passados como parâmetro, o que ocasiona sucessivos envios em chamadas de sistema até que todos os bytes sejam enviados.

'''


HOST = input('IP do servidor: ') # 127.0.0.1
PORT = 50000 # porta do servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:
    socket_client.connect((HOST, PORT))
    print(f'Conectado ao servidor em {HOST} {PORT}')
    mensage = input('Mensage: ')
    socket_client.sendall(mensage.encode())
    data = socket_client.recv(4096)
    print('Mensagem recebida do servidor:', data.decode())

# O socket será fechado automaticamente ao sair do bloco with

