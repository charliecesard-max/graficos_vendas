import pandas as pd


def estoque_de_itens():
    id = input('Digite o Código do produto:')
    nome = input('Digite a Descrição do item: ')
    categoria = input('Digite a categoria do produto:')
    unidade = input('Digite a unidade do produto: ')
    estoque[id] = {'id': id, 'nome': nome, 'categoria': categoria, 'unidade': unidade}
    print(f'Produto {nome} cadastrado com sucesso!')
    
    print('Estoque Atual')
    for id, dados in reversed(list(estoque.items())):
        nome = dados['nome']
        categoria = dados['categoria']
        unidade = dados['unidade']
        print(f'{id}, {nome}, {categoria}, {unidade}')


estoque = {}

opcao = input('Deseja continuar o cadastro ? [S/N] ').upper()

while opcao == 'S':
    
    estoque_de_itens()
    
    opcao = input('Deseja cadastrar mais um pedido?  [S/N]? ').upper()

df = pd.DataFrame(list(estoque.values()))
df.to_excel('estoque.xlsx', index=False)
print('Saindo...')

exportar = input('Deseja exportar o estoque para Excel? [S/N] ').upper()
if exportar == 'S':
    df = pd.DataFrame(list(estoque.values()))
    df.to_excel('estoque.xlsx', index=False)
    print('Estoque exportado para estoque.xlsx')