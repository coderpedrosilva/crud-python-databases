import pg # biblioteca pygresql

def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = pg.DB(
            dbname='ppostgresql',
            host='localhost',
            user='postgres',
            passwd='123456'
        )
        return conn
    except pg.OperationalError as e:
        print(f'Erro na conexão ao PostgreSQL Server: {e}')


def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    if conn is None:
        return

    try:
        query = 'SELECT * FROM produtos'
        result = conn.query(query)
        produtos = result.getresult()

        if len(produtos) > 0:
            print('Listando produtos...')
            print('--------------------')
            for produto in produtos:
                print(f'ID: {produto[0]}')
                print(f'Produto: {produto[1]}')
                print(f'Preço: {produto[2]}')
                print(f'Estoque: {produto[3]}')
                print('--------------------')
        else:
            print('Não existem produtos cadastrados.')
    finally:
        desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    """  
    conn = conectar()
    if conn is None:
        return
    
    try:
        print('Inserindo produto...')
        nome = input('Informe o nome do produto: ')
        preco = float(input('Informe o preço do produto: '))
        estoque = int(input('Informe a quantidade em estoque: '))

        query = f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})"
        conn.query(query)
        conn.commit()
        print('Produto inserido com sucesso.')
    except Exception as e:
        print(f'Erro ao inserir o produto: {e}')
    finally:
        desconectar(conn)

def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    if conn is None:
        return
    
    try:
        codigo = int(input('Informe o código do produto: '))
        nome = input('Informe o nome do produto: ')
        preco = float(input('Informe o preço do produto: '))
        estoque = int(input('Informe a quantidade em estoque: '))

        query = f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}"
        conn.query(query)
        
        print(f'Produto {nome} foi atualizado com sucesso.')
    except Exception as e:
        print(f'Erro ao atualizar o produto: {e}')
    finally:
        desconectar(conn)

def deletar():
    """
    Função para deletar um produto
    """  
    conn = conectar()
    if conn is None:
        return
    
    try:
        codigo = int(input('Informe o código do produto: '))
        query = f"DELETE FROM produtos WHERE id={codigo}"
        conn.query(query)
        print(f'Produto excluído com sucesso.')
    except Exception as e:
        print(f'Erro ao excluir o produto: {e}')
    finally:
        desconectar(conn)

def menu():
    """
    Função para gerar o menu inicial
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
