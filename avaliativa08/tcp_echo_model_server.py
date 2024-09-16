import socket, platform
from funcoes_socket import *
from funcao_tracrt import *

sisOp = platform.system()

print('Recebendo Mensagens...\n\n')

# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligando o socket a porta
tcp_socket.bind((HOST_SERVER, SOCKET_PORT)) 

# Máximo de conexões enfileiradas
tcp_socket.listen(MAX_LISTEN)

while True:
    # Aceita a conexão com o cliente
    conexao, cliente = tcp_socket.accept()
    print('Conectado por: ', cliente)
    while True:
        mensagem = conexao.recv(BUFFER_SIZE)
        if not mensagem: break
        mensagem_decode = mensagem.decode(CODE_PAGE)
        print(cliente, mensagem_decode)
        
        # Devolvendo uma mensagem (echo) ao cliente
        mensagem_executar = tracert_to_url(mensagem, sisOp)
        cria_arquivo(mensagem_decode, mensagem_executar)
        print(mensagem_executar)
        mensagem_retorno = 'Devolvendo...' + mensagem.decode(CODE_PAGE) + '\nJá está salvo do arquivo forma de JSON.'
        conexao.send(mensagem_retorno.encode(CODE_PAGE))

    print('Finalizando Conexão do Cliente ', cliente)
    conexao.close()
