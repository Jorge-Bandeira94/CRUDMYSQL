

"""1. Instalar o driver para que o Python se conecte ao MySQL através do (pip install mysqlclient) na aba TERMINAL
2. criar o banco e as tabelas no MySQL workbench"""
"""Importando o driver do MySQL para que possamos fazer a conexão com o banco"""

import MySQLdb


def conectar():
    print('Conectando ao servidor...')

    """Aqui estamos configurando o acesso automatico ao banco de dados e especificando com o comando connect que devemos conectar ao db 
    (nome do banco), com o host X para o usuário cadastrado (no MySQL está como root) e senha"""
    try:
        conn = MySQLdb.connect(
            db='python_crud_projeto',
            host='localhost',
            user='root',
            passwd='root'
        )

        """O return serve para que ao executar o try a variável "conn" definida logo acima seja executada, caso haja algum problema
        receberemos o erro que está definido em except"""

        return conn
    except MySQLdb.Error as e:
        print(f'Erro na conexão ao MySQL Server: {e}')


def desconectar(conn):
    """ Esta função irá receber a variável criada anteriormente 'conn' para ser usada aqui."""
    print('Desconectando do servidor...')
    """Especificando que, se conn estiver sendo executada, finalize-a com o comando close()"""
    if conn:
        conn.close()


def listar():

    """Aqui entram as funções de SELECT no MySQL"""

    """Adicionamos a variavel de conexão ao banco para que possamos utiliza-lo e também uma variavel cursor para que
    possamos trabalhar com o banco de dados, é ele que executa os dados"""

    conn = conectar()
    cursor = conn.cursor()

    """Usamos o cursor para dar comando SQL como visto no MySQL, aqui estamos usando um comando DQL"""

    cursor.execute('SELECT * FROM produtos')

    """Criamos esta variável para que o resultado do cursor.execute seja jogado numa lista a partir do comando
    .fetchall() que será impressa em tela"""

    produtos = cursor.fetchall()

    """Verificando se a lista está cheia ou vazia, caso a lista seja maior que 0, imprimirá todos os dados abaixo,
    caso não seja, uma mensagem será exibida informando que não há produtos"""

    if len(produtos) > 0:
        print('Listando produtos...')
        print('....................')
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'Produto: {produto[1]}')
            print(f'Preco: {produto[2]}')
            print(f'Estoque: {produto[3]}')
            print('................')
    else:
        print("Não existem produtos cadastrados")

    """Será feita a desconexão após serem executados os comandos acima"""

    desconectar(conn)


def inserir():

    print('Inserindo produto...')
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe a quantidade em estoque: '))

    """Aqui estamos dando ao cursosr a função de inserior do SQL"""

    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")

    """Concluir a transação com commit() para que seja salva"""

    conn.commit()

    """Se houver uma linha contada pelo cursos, ele ira retornar a mensagem, caso de algum erro, não haverá linhas"""

    if cursor.rowcount == 1:
        print(f'O produtos {nome} foi inserido com sucesso')
    else:
        print('Não foi possível inserir o produtos')
    desconectar(conn)


def atualizar():

    print('Atualizando produto...')
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto: '))
    nome = input('Novo nome do produto: ')
    preco = float(input('Informe o novo preço: '))
    estoque = int(input('informe a nova quantidade em estoque: '))

    cursor.execute(f"UPDATE produtos SET nome= '{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto foi atualizado com sucesso')
    else:
        print('Erro na atualização do produto')
    desconectar(conn)


def deletar():

    print('Deletando produto...')
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Digite o codigo do produto que deseja apagar: '))

    cursor.execute(f'DELETE FROM produtos WHERE id ={codigo}')
    """Salvando a ação com commit()"""
    conn.commit()

    """Como sabemos se foi deletado ou não? Usamos a contagem do cursor para nos informar"""
    if cursor.rowcount == 1:
        print('Produto deletado')
    else:
        print('Não foi possível deletar este produto')
    desconectar(conn)

def menu():
    """
    Aqui fica nosso menu inicial, e associamos os numeros digitaos a função() que desejamos executar
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
