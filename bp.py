# lista de nomes
nomes = ['Alex', 'Eduardo', 'Maria', 'Mariana', 'João', 'José', 'Joana', 'Fernanda', 'Fulano', 'Cicrano', 'Beltrano', 'Connor', 'Corona', 'Cecília', 'Alexandre']

#usuário informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado:').capitalize()

# retorna o índice (posição) do nome pesquisado
try:
    indice = nomes.index(nome)

    # verifica se o nome está na lista ou não
    print(f'Nome encontrado: {nome} no índice {indice}.')
except:
    print(f'{nome} não encontrado na lista.')