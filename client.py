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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:
        socket_client.connect(ADDR)
        print(f'Conectado ao servidor em {ADDR[0]} {ADDR[1]}')
        chances = 5
        if chances == 5:
                print('Um número aleatório de 0 a 100 foi escolhido.')
        
        while True:
            mensage = int(input('Digite um número entre 0 e 100: '))
            socket_client.sendall(str(mensage).encode())
            data = socket_client.recv(4096)
            data = data.decode()
            print('Servidor: ', data)

            if data == f"Parabéns! Você acertou o número ({mensage})!":
                print("Encerrando a conexão com o servidor...")
                break
            
            if data == "Suas chances acabaram." and chances == 0:
                print("Encerrando a conexão com o servidor...")
                break
            
            chances = chances-1
                
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
    print('\t0 - Logar em um servidor\n\t1 - Sair do programa\n')
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