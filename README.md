# JOGO do Acerte o numero

O jogo segue a seguinte ideia, a máquina sorteia um numero de 0 a 100 de forma aleatória e ao se você terá 5 chances para poder acertar o numero
o jogo está utilizando sockets do tipo TCP em python para estabelecer a conexão do cliente com o servior, tanto o cliente como o servidor utilizão conexão TCP,
ao estabelecer conexão o servidor cria uma thread para cada jogador, ou seja, nenhum jogador joga com outro usuário que está conectado.

## Instalação

Para realizar a instalação será necesário que você tenha o [Python](https://www.python.org/downloads/), [Git](https://git-scm.com/) e o Editor de código de sua preferencia(para facilitar a visualização e edição do ip do servidor, caso queira deixar ele acessivel para outros computadores poderem acessar) recomendamos [VScode](https://code.visualstudio.com/).

Ao final de tudo instalado, você deverá clonar o repositório.

para facilitar, tudo estará nos comandos a seguir.

os comandos  deverão ser realizado no terminal do GIT

- $ mkdir JOGO

- $ cd JODO

- $ git clone https://github.com/josaugusto/Projeto-de-Redes.git

- $ cd Projeto-de-Redes

os comandos acima criou uma pasta chamada JOGO entrou nela e clonou o repositório

## Uso

Para jogar será necessário que você tenha aberto a pasta do jogo no seu editor de cógido, caso tenha o VScode instaldo 
e no git você parou no ultimo passo da instrução de instalação basta dar o seguinte comando

- $ code .

e o projeto será aberto no VScode.

para rodar o jogo você deverá abrir dois terminais no VScode, sendo um para o servidor e um para o cliente, lembre-se, o terminal do servidor não deve ser fechado durante a partida, caso contrário o jogo será finalizado.

Ao abrir os dois terminais você deverá digitar o seguintes comandos

no primeiro terminal:

- $ python server.py

e no segundo terminal:

- $ python client.py

ao colocar a opção de logar no servidor, você deverá informar o IP do servidor que é o localhost sendo assim você deverá informar 

- $ 127.0.0.1

caso você deseje alterar o IP do servidor para jogar de outro pc dentro da própria rede é só alterar no código a linha 6, trocando o nome localhost pelo ip de sua máquina. porém deverá manter as aspas simples ''.
