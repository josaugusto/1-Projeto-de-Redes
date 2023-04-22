import socket
import os
from time import sleep
import threading
from ipaddress import ip_address


def main():
    while True:
        try:
            HOST = input('IP do servidor: ') # 127.0.0.1
            ip_address(HOST)
            break
        except ValueError:
            print('Endereço IP inválido.\nTente novamente.')

    while True:
        try:
            PORT = int(input('Porta: '))
            break
        except ValueError: 
            print('A porta tem que ser um número inteiro.\nTente novamente')


    Thread = threading.Thread(target=client, args=((HOST, PORT),))
    Thread.start()


def client(ADDR):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_cliet:
        socket_cliet.connect(ADDR)
        print(f'Conectado ao servidor em {ADDR[0]} {ADDR[1]}')
        mensage = input('Mensage: ')
        socket_cliet.sendall(mensage.encode())
        data = socket_cliet.recv(4096)
        print('Mensagem recebida do servidor:', data.decode())
    sleep(5) # foi só para não apagar tudo sem ver a mensagem.
    menu()


def menu():
    os.system('cls')
    print('\tTela inicial do programa')
    print('-'*40)
    print('Selecione uma das opções abaixo:\n')
    print('\t0 - Logar em um servidor\n\t1 - Sair do programa\n')
    print('-'*40)

    while True:
        op = input('-> ').strip()
        if op == '0': 
            break
        elif op == '1':
            return
        else:
            print('Opção invalida!')

    os.system('cls')
    main()
    
menu()
