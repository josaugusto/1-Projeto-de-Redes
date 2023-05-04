import socket
import os
from helpers import get_valid_ip, get_valid_port
from time import sleep


def main():
    HOST = get_valid_ip()
    PORT = get_valid_port()
    client((HOST, PORT))


def client(ADDR):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:
        socket_client.connect(ADDR)
        print(f'Conectado ao servidor em {ADDR[0]} {ADDR[1]}')

        chances = 5
        if chances == 5:
                print('Um número aleatório de 0 a 100 foi gerado.')
        
        while True:
            mensage = input('Digite um número entre 0 e 100: ')
            socket_client.sendall(mensage.encode())
            chances-=1
            data = socket_client.recv(4096)
            data = data.decode()
            print('Servidor: ', data)

            if data == f"Parabéns! Você acertou o número ({mensage})!":
                print("Encerrando a conexão com o servidor...")
                break
            
            if data == 'Suas chances acabaram.' and chances == 0:
                print("Encerrando a conexão com o servidor...")
                break
    sleep(3)  # foi só para não apagar tudo sem ver a mensagem.
    menu()


def menu():
    if os.name == 'nt':
        clear_cmd = 'cls'
    else:
        clear_cmd = 'clear'

    os.system(clear_cmd)
    print('\tTela inicial do programa')
    print('-' * 40)
    print('Selecione uma das opções abaixo:\n')
    print('\t0 - Logar no servidor\n\t1 - Sair do programa\n')
    print('-' * 40)

    while True:
        op = input('-> ').strip()
        if op == '0':
            break
        elif op == '1':
            return
        else:
            print('Opção invalida!')

    os.system(clear_cmd)
    main()
menu()      
