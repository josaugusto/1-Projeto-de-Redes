from ipaddress import ip_address

def get_valid_ip():
    while True:
        try:
            ip = input('IP do servidor: ')
            ip_address(ip)
            return ip
        except ValueError:
            print('Endereço IP inválido.\nTente novamente.')

def get_valid_port():
    while True:
        try:
            port = int(input('Porta: '))
            return port
        except ValueError: 
            print('A porta tem que ser um número inteiro.\nTente novamente.')