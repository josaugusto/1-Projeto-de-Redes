from ipaddress import ip_address

def get_valid_ip():
    while True:
        try:
            ip = input('IP do servidor: ')
            ip_address(ip)  # verificando se o ip é valido, caso não, sobe o erro "ValueError"
            return ip       # retorna o ip se tiver tudo certo
        except ValueError:
            print('Endereço IP inválido.\nTente novamente.')    # tenta novamente caso esteja errado

def get_valid_port():
    while True:
        try:
            port = int(input('Porta: '))    # pede a porta para conexão
            return port                     # retorna a porta caso seja um numero inteiro, do contrário sobe o erro ValueError
        except ValueError: 
            print('A porta tem que ser um número inteiro.\nTente novamente.')
